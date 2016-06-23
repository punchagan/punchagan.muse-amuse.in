(add-to-list 'load-path
             (car (directory-files "~/.emacs.d/elpa/" t "^ob-ipython-20.*")))
(add-to-list 'load-path
             (car (directory-files "~/.emacs.d/elpa/" t "^dash-functional-20.*")))
(add-to-list 'load-path
             (car (directory-files "~/.emacs.d/elpa/" t "^dash-20.*")))
(add-to-list 'load-path
             (car (directory-files "~/.emacs.d/elpa/" t "^s-20.*")))
(add-to-list 'load-path
             (car (directory-files "~/.emacs.d/elpa/" t "^f-20.*")))
(require 'ob-ipython)

(add-to-list 'org-pygments-language-alist '("ipython" . "python"))

(setq org-export-babel-evaluate nil)
