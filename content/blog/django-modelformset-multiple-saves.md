---
title: "Django ModelFormSet and multiple saves"
date: 2020-01-08T09:45:00+05:30
tags: ["blag", "software", "python", "django"]
draft: false
---

A friend and I were trying to [use the Django ModelFormSets](https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/#using-a-model-formset-in-a-view) in a project, and we
ran into a subtle bug that took a little big of digging into the Django code to
identify and work around.


## The Bug {#the-bug}

We weren't really familiar with Django's `FormSet` or `ModelFormSet`, when we
started. We began by reading the documentation to get started.

The Django docs had [an example](https://docs.djangoproject.com/en/2.2/topics/forms/modelforms/#using-a-model-formset-in-a-view) that looked straight-forward, and showed how to
use `ModelFormSet`.

```python
  def manage_authors(request):
      AuthorFormSet = modelformset_factory(Author, fields=('name', 'title'))
      if request.method == 'POST':
          formset = AuthorFormSet(request.POST, request.FILES)
          if formset.is_valid():
              formset.save()
              # do something.
      else:
          formset = AuthorFormSet()
      return render(request, 'manage_authors.html', {'formset': formset})
```

-   You create a `ModelFormSet` class using the `modelformset_factory` using the
    required model, and the required fields.

-   Use the data from a `POST` to create an instance of the class from above.

-   Save the data if the formset validates, and we are done!

We tweaked the example to our needs, and it worked for us. Mostly.

A user reported that after saving the form once with some data, trying to save
more data didn't work! The form would try to save the data already saved in the
last save, and fail validation that required some of the fields to be unique.

On the second save, the data which was saved during the last save was still
being treated as newly filled in data!

This also caused newly filled-in data during the second save to be lost forever.
The user was forced to reload the page and re-enter the data.


## The Why {#the-why}

The way Django keeps track of newly filled-in data in the form along with
multiple levels of caching causes this bug to manifest.


### `ModelFormSet` `queryset` argument {#modelformset-queryset-argument}

`AuthorFormSet` (or any `ModelFormSet` created using the `modelformset_factory`)
takes an additional optional argument `queryset`. This argument can be used to
choose specific rows in the DB that need to be used to populate the initial form
rows, if any. If no `queryset` is specified, all the objects in the DB are used.


### `FormSet`  metadata {#formset-metadata}

First, metadata about the form is saved in a few hidden input fields (called the
`ManagementForm`). This hidden form keep tracks of metadata like the total
number of forms to show, initial form count and the minimum & maximum number of
forms to display.

```html
  <input type="hidden" name="form-TOTAL_FORMS" value="19" id="id_form-TOTAL_FORMS">
  <input type="hidden" name="form-INITIAL_FORMS" value="7" id="id_form-INITIAL_FORMS">
  <input type="hidden" name="form-MIN_NUM_FORMS" value="0" id="id_form-MIN_NUM_FORMS">
  <input type="hidden" name="form-MAX_NUM_FORMS" value="1000" id="id_form-MAX_NUM_FORMS">
```

Initial form count is the count of the number of forms that are pre-filled using
data from the DB -- essentially, the length of the `queryset`


### Metadata does not change {#metadata-does-not-change}

When the `ModelFormSet` is used as described in the documentation, the metadata
in the `ManagementForm` doesn't get updated when the form is re-rendered in the
response to a successful `POST` request. If one form with new data was
successfully saved, the number of initial forms in the re-rendered form must go
up by 1, but it doesn't.


### Queryset caching problem {#queryset-caching-problem}

Django has caching at the queryset level which means that the queryset doesn't
get updated with the newly created instances, even if they match the query that
the queryset uses.

```python
  formset = AuthorFormSet(request.POST, request.FILES, queryset=existing_authors)
```

`existing_authors` is a queryset that looks for a specific set of authors in the
DB, or may be all the authors in the DB, if that's what the form needs to do.

So, when a formset has been submitted, and some new rows have been created in
the model's table, the new rows don't automatically get added to the `queryset`
since it the results fetched from the DB are cached by the `queryset`. We need
to create a new `queryset` for it to include the newly created rows.

These two levels of caching combined make the bug manifest, as it does. I'm not
yet sure what the correct "fix" for this is, but we ended up using a work-around
-- create a new formset when returning from a successful `POST`.


## The Work-Around {#the-work-around}

We instantiate a new `ModelFormSet` instance when returning the form, on a
successful `POST`. This means, the `ManagementForm` is recreated for the new
formset and has the correct metadata about the form, even when being rendered in
the response of a successful `POST`.

The code in the example in Django docs, would look something like the one below:

```python
  def manage_authors(request):
      AuthorFormSet = modelformset_factory(Author, fields=('name', 'title'))
      if request.method == 'POST':
          formset = AuthorFormSet(request.POST, request.FILES)
          if not formset.is_valid():
              return render(request, 'manage_authors.html', {'formset': formset})
          else:
              formset.save()

      formset = AuthorFormSet()
      return render(request, 'manage_authors.html', {'formset': formset})
```

This blog post should probably become a PR or an issue, but I'm not familiar
with how contributing to Django works. This blog post is an attempt to
understand the issue better, and potentially help others who get bit by it.

<div style="font-size:small;" class="reviewers">
  <div></div>

Thanks to [Shantanu](http://baali.muse-amuse.in) for reading drafts of this post.

</div>
