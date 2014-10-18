#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <memory>

namespace {

std::string clean_html(std::string html){
    //Remove code
    auto pos = html.find("```");
    while(pos != std::string::npos){
        html.erase(html.begin() + pos, html.begin() + html.find("```", pos + 1) + 3);
        pos = html.find("```");
    }

    //Remove the content of the <pre>
    pos = html.find("<pre>");
    while(pos != std::string::npos){
        html.erase(html.begin() + pos, html.begin() + html.find("</pre>") + 6);
        pos = html.find("<pre>");
    }
    
    std::string clean;

    //Remove all HTML tags
    for(;;){
        std::string::size_type  startpos;

        startpos = html.find('<');
        if(startpos == std::string::npos){
            clean += html;
            break;
        }

        // handle the text before the tag    
        if(0 != startpos){
            clean += html.substr(0, startpos);
            html = html.substr(startpos, html.size() - startpos);
            startpos = 0;
        }

        //  skip all the text in the html tag
        std::string::size_type endpos;
        for(endpos = startpos; endpos < html.size() && html[endpos] != '>'; ++endpos){
            // since '>' can appear inside of an attribute string we need
            // to make sure we process it properly.
            if(html[endpos] == '"'){
                endpos++;
                while(endpos < html.size() && html[endpos] != '"'){
                    endpos++;
                }
            }
        }

        //  Handle text and end of html that has beginning of tag but not the end
        if(endpos == html.size()){
            html = html.substr(endpos, html.size() - endpos);
            break;
        } else {
            //  handle the entire tag
            endpos++;
            html = html.substr(endpos, html.size() - endpos);
        }
    }

    return clean;
}

void read_metadata(const std::vector<std::string>& files, std::vector<std::string>& titles, std::vector<std::string>& keywords, std::vector<std::string>& urls){
    for(size_t i = 0; i < files.size(); ++i){
        auto file = files[i];

        file.replace(file.begin() + file.rfind('.'), file.end(), ".meta");

        std::ifstream stream(file);
        std::string line;
        std::string slug;

        if(files[i].find(".rst") == std::string::npos){
            getline(stream, line);
            titles[i] = line;

            getline(stream, line);
            slug = line;

            //Ignore the date
            getline(stream, line);

            getline(stream, line);
            keywords[i] = line;
        } else {
            getline(stream, line);
            titles[i] = line.substr(10);

            getline(stream, line);
            slug = line.substr(9);

            //Ignore the date
            getline(stream, line);

            getline(stream, line);
            keywords[i] = line.substr(9);
        }

        std::string url = file;
        url.replace(url.begin(), url.begin() + 2, "");
        url.replace(url.begin() + url.rfind('/') + 1, url.end(), slug);

        urls[i] = url + ".html";
    }
}

void clean_string(std::string& clean){
    //Remove parenth
    std::replace(clean.begin(), clean.end(), '(', ' ');
    std::replace(clean.begin(), clean.end(), ')', ' ');

    //Remove markdown
    std::replace(clean.begin(), clean.end(), '*', ' ');
    std::replace(clean.begin(), clean.end(), '#', ' ');
    std::replace(clean.begin(), clean.end(), '[', ' ');
    std::replace(clean.begin(), clean.end(), ']', ' ');

    //Remove punctuation
    std::replace(clean.begin(), clean.end(), ',', ' ');
    std::replace(clean.begin(), clean.end(), '.', ' ');
    std::replace(clean.begin(), clean.end(), ';', ' ');
    std::replace(clean.begin(), clean.end(), ':', ' ');
    std::replace(clean.begin(), clean.end(), '!', ' ');
    std::replace(clean.begin(), clean.end(), '"', ' ');

    //Remove carriage returns and tabs
    std::replace(clean.begin(), clean.end(), '\r', ' ');
    std::replace(clean.begin(), clean.end(), '\n', ' ');
    std::replace(clean.begin(), clean.end(), '\t', ' ');
}

void compute_frequencies(const std::string& source, std::unordered_map<std::string, std::size_t>& tf, std::unordered_set<std::string>& word_set, std::size_t factor){
    auto str = source;

    clean_string(str);

    std::stringstream ss(str);
    do {
        std::string word;
        ss >> word;

        word.erase(std::remove(word.begin(), word.end(), ' '), word.end());

        std::transform(word.begin(), word.end(), word.begin(), ::tolower);

        tf[word] += factor;
        word_set.insert(word);
    } while(ss);
}

} //end of anonymous namespace

int main(int argc, char* argv[]){
    if(argc < 2){
        return 1;
    }

    std::vector<std::string> files;
    for(int i = 1; i < argc; ++i){
        files.emplace_back(argv[i]);
    }

    std::unordered_set<std::string> word_set;
    std::vector<std::unordered_map<std::string, std::size_t>> tf_tmp(files.size());

    std::vector<std::string> titles(files.size());
    std::vector<std::string> keywords(files.size());
    std::vector<std::string> urls(files.size());

    read_metadata(files, titles, keywords, urls);

    for(size_t i = 0; i < files.size(); ++i){
        std::ifstream stream(files[i]);

        std::string html_contents(
            (std::istreambuf_iterator<char>(stream)),
            std::istreambuf_iterator<char>());

        auto contents = clean_html(html_contents);

        compute_frequencies(contents, tf_tmp[i], word_set, 1);
        compute_frequencies(keywords[i], tf_tmp[i], word_set, 2);
        compute_frequencies(titles[i], tf_tmp[i], word_set, 3);
    }

    std::vector<std::string> words;
    std::copy(word_set.begin(), word_set.end(), std::back_inserter(words));
    
    std::vector<double> idf(words.size());

    std::vector<std::vector<std::size_t>> tf(files.size());
    std::vector<std::vector<double>> tf_idf(files.size());

    //Compute Term Frequency

    for(size_t i = 0; i < files.size(); ++i){
        tf[i].resize(words.size());
        tf_idf[i].resize(words.size());

        for(size_t w = 0; w < words.size(); ++w){
            tf[i][w] = tf_tmp[i][words[w]];
        }
    }

    //Compute Inverse Document Frequency

    for(size_t w = 0; w < words.size(); ++w){
        std::size_t n = 0;
        for(size_t i = 0; i < files.size(); ++i){
            n += tf[i][w] > 0 ? 1 : 0;
        }

        idf[w] = log(files.size() / (1.0 + static_cast<double>(n)));
    }

    //Compute TF-IDF
        
    for(size_t i = 0; i < files.size(); ++i){
        for(size_t w = 0; w < words.size(); ++w){
            tf_idf[i][w] = tf[i][w] * idf[w];
        }
    }

    //Compute the matrix of Cosine Similarities

    std::unique_ptr<double[]> similarities(new double[files.size() * files.size()]);
    
    for(size_t i = 0; i < files.size(); ++i){
        similarities[i * files.size() + i] = 1;

        for(size_t j = i+1; j < files.size(); ++j){
            double cosine_similarity = 0.0;
            double n1 = 0.0;
            double n2 = 0.0;

            for(size_t w = 0; w < words.size(); ++w){
                cosine_similarity += tf_idf[i][w] * tf_idf[j][w];
                n1 += tf_idf[i][w] * tf_idf[i][w];
                n2 += tf_idf[j][w] * tf_idf[j][w];
            }

            cosine_similarity /= sqrt(n1) * sqrt(n2);

            similarities[i * files.size() + j] = cosine_similarity;
            similarities[j * files.size() + i] = cosine_similarity;
        }
    }

    //Generate HTML
        
    std::vector<std::size_t> related(files.size());
    std::iota(related.begin(), related.end(), 0);
    
    for(size_t i = 0; i < files.size(); ++i){
        std::sort(related.begin(), related.end(), [i,&similarities, &files](size_t j1, size_t j2) -> bool {
            return similarities[i * files.size() + j1] > similarities[i * files.size() + j2];
        });

        std::ofstream file(files[i] + ".related.html");

        file << "<ol>\n";

        for(size_t j = 0; j < related.size() && j < 6; ++j){
            auto other = related[j];

            if(other != i){
                file << "<li><a href=\"" << urls[other] << "\">" << titles[other] << "</a></li>\n";
            }
        }

        file << "</ol>\n" << std::endl;
    }

    return 0;
}
