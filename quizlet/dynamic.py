from IPython.core.display import display, Javascript, HTML
import string
import random
import pkg_resources


def display_questions_dynamic (url, num=1_000_000, shuffle_questions=False,
                                   shuffle_answers=True):

    resource_package = __name__

    letters = string.ascii_letters
    div_id= ''.join(random.choice(letters) for i in range(12))
    #print(div_id)

    mydiv='<div id="'+ div_id + '" data-shufflequestions="' + str(shuffle_questions) +'"'
    mydiv+=' data-shuffleanswers="' + str(shuffle_answers) +'"'
    mydiv+=' data-numquestions="' + str(num) +'">'

    styles="<style>"
    css=pkg_resources.resource_string(resource_package, "styles.css")
    styles+=css.decode("utf-8")
    styles+="</style>"
    
    
    script='<script type="text/Javascript">'
    
    script+='//var mydiv=document.getElementById("testDIV");'
    script+='//console.log(mydiv);'
    
    #display(HTML(mydiv + script))
    #return

    # print(__name__)
    helpers=pkg_resources.resource_string(resource_package, "helpers.js")
    script+=helpers.decode("utf-8")

    multiple_choice=pkg_resources.resource_string(resource_package, "multiple_choice.js")
    script+=multiple_choice.decode("utf-8")

    numeric=pkg_resources.resource_string(resource_package, "numeric.js")
    script+=numeric.decode("utf-8")

    show_questions = pkg_resources.resource_string(resource_package, "show_questions.js")
    script+=show_questions.decode("utf-8")


    script+='''
    //console.log(element);

            fetch("'''
    script_end='''")
      .then(response => response.json())
      .then(json => show_questions(json, '''
      #.then(json => console.log( '''

    script_end+=div_id
    script_end+= ''')
    );


    </script>
      '''
    javascript=script + url + script_end
    display(HTML(mydiv + styles +  javascript))

