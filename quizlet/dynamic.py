from IPython.core.display import display, Javascript, HTML
import string
import random
import pkg_resources


def display_questions_dynamic (url, num=1_000_000, shuffle_questions=False,
                                   shuffle_answers=True):

    letters = string.ascii_letters
    div_id= ''.join(random.choice(letters) for i in range(12))
    #print(div_id)

    mydiv='<div id="'+ div_id + '" data-shufflequestions="' + str(shuffle_questions) +'"'
    mydiv+=' data-shuffleanswers="' + str(shuffle_answers) +'"'
    mydiv+=' data-numquestions="' + str(num) +'">'
    
    
    script='<script type="text/Javascript">'
    
    script+='//var mydiv=document.getElementById("testDIV");'
    script+='//console.log(mydiv);'
    
    #display(HTML(mydiv + script))
    #return

    # print(__name__)
    resource_package = __name__
    helpers=pkg_resources.resource_string(resource_package, "helpers.js")
    # print(helpers)



    script+=helpers.decode("utf-8")

    script+='''
    //console.log(element);

    function check() {
        var id=this.id.split('-')[0];

        //console.log("In check(), id="+id);
        //console.log(event.srcElement.id)           
        //console.log(event.srcElement.dataset.correct)   
        //console.log(event.srcElement.dataset.feedback)

        var answers= event.srcElement.parentElement.children;
        //console.log(answers);
        
        // Split behavior based on multiple choice vs many choice:
        var fb = document.getElementById("fb"+id);
        if (fb.dataset.numcorrect==1) {
            for (var i = 0; i < answers.length; i++) {
                var child=answers[i];
                child.style.background="#fafafa";
            }



            fb.textContent=event.srcElement.dataset.feedback;
            if (event.srcElement.dataset.correct=="true")   {
                // console.log("Correct action");
                event.srcElement.style.background="#d8ffc4";
                fb.style.color="#009113";
            } else {
                //console.log("Error action");
                event.srcElement.style.background="#ffe8e8";
                fb.style.color="#DC2329";
            }
        }
        else {
            //console.log("Many choice not implemented yet");
            var reset = false;
            if (event.srcElement.dataset.correct=="true" )   {
                if (event.srcElement.dataset.answered<=0) {
                    if (fb.dataset.answeredcorrect<0) {
                        fb.dataset.answeredcorrect=1;
                        reset=true;
                    } else {
                       fb.dataset.answeredcorrect++;
                    }
                    if (reset) {
                        for (var i = 0; i < answers.length; i++) {
                            var child=answers[i];
                            child.style.background="#fafafa";
                            child.dataset.answered=0;
                        }
                    }
                    event.srcElement.style.background="#d8ffc4";
                    event.srcElement.dataset.answered=1;
                    fb.style.color="#009113";

                }
            } else {
                if (fb.dataset.answeredcorrect>0) {
                    fb.dataset.answeredcorrect=-1;
                    reset=true;
                } else {
                   fb.dataset.answeredcorrect--;
                }

                if (reset) {
                    for (var i = 0; i < answers.length; i++) {
                        var child=answers[i];
                        child.style.background="#fafafa";
                        child.dataset.answered=0;
                    }
                }
                event.srcElement.style.background="#ffe8e8";
                fb.style.color="#DC2329";
            }


            var numcorrect=fb.dataset.numcorrect;
            var answeredcorrect=fb.dataset.answeredcorrect;
            if (answeredcorrect>=0) {
                fb.textContent=event.srcElement.dataset.feedback + " ["  + answeredcorrect + "/" + numcorrect + "]";
            } else {
                fb.textContent=event.srcElement.dataset.feedback + "["  + 0 + "/" + numcorrect + "]";
            }


        }

        

    }

    function make_mc(qa, shuffle_answers, aDiv, id) {
             var shuffled;
            if (shuffle_answers=="True") {
                //console.log(shuffle_answers+" read as true");
                shuffled=getRandomSubarray(qa.answers, qa.answers.length);
            } else {
                //console.log(shuffle_answers+" read as false");
                shuffled=qa.answers;
            }
        

            var num_correct=0;


            
            shuffled.forEach((item, index, ans_array) => {
                //console.log(answer);
                
                // Make input element
                var inp = document.createElement("input");
                inp.type="radio";
                inp.id="quizo"+id+index;
                inp.style="display:none;";
                aDiv.append(inp);
                
                //Make label for input element
                var lab = document.createElement("label");
                lab.style="background: #fafafa; border: 1px solid #eee;  border-radius: 10px; padding: 10px; font-size: 16px; cursor: pointer; text-align: center;";
                lab.id=id+ '-' +index;
                lab.onclick=check;
                lab.textContent=item.answer;
                
                // Set the data attributes for the answer
                lab.setAttribute('data-correct', item.correct);
                if (item.correct) {
                    num_correct++;
                }
                lab.setAttribute('data-feedback', item.feedback);
                lab.setAttribute('data-answered', 0);

                aDiv.append(lab);
                
                
            });

    return num_correct;
   
    }
    
    function parse (json, mydiv) {
    //var mydiv=document.getElementById(myid);
    var shuffle_questions=mydiv.dataset.shufflequestions;
    var num_questions=mydiv.dataset.numquestions;
    var shuffle_answers=mydiv.dataset.shuffleanswers;
    
    if (num_questions>json.length) {
        num_questions=json.length;
    }
    
    var questions;
    if ( (num_questions<json.length) || (shuffle_questions=="True") ) {
            //console.log(num_questions+","+json.length);
            questions=getRandomSubarray(json, num_questions);
        } else {
            questions=json;
        }
    
        //console.log("SQ: "+shuffle_questions+", NQ: " + num_questions + ", SA: ", shuffle_answers);
        
        // Iterate over questions
        questions.forEach((qa, index, array) => {
            //console.log(qa.question); 

            var id = makeid(8);
            //console.log(id);


            // Create Div to contain question and answers
            var iDiv = document.createElement('div');
            iDiv.id = 'quizWrap'+id+index;
            iDiv.style='max-width: 600px; margin: 0 auto;padding-bottom: 30px;';
            mydiv.appendChild(iDiv);
            // iDiv.innerHTML=qa.question;

            // Create div to contain question part
            var qDiv = document.createElement('div');
            qDiv.id="quizQn"+id+index;
            qDiv.style='padding: 20px;color: #fafafa;font-size: 20px;border-radius: 10px; background: #6F78FF;';
            //qDiv.innerHTML=qa.question;
            qDiv.textContent=qa.question;
            iDiv.append(qDiv);

            // Create div to contain answer part
            var aDiv = document.createElement('div');
            aDiv.id="quizAns"+id+index;
            aDiv.style="margin: 10px 0; display: grid; grid-template-columns: auto auto;grid-gap: 10px;";
            iDiv.append(aDiv);

            console.log(qa.type);

            var num_correct;
    if ((qa.type=="multiple_choice") || (qa.type=="many_choice")){
       num_correct=make_mc(qa, shuffle_answers, aDiv, id);
    }


            //Make div for feedback
            var fb = document.createElement("div");
            fb.id="fb"+id;
            fb.style="font-size: 20px;text-align:center;";
            fb.setAttribute("data-answeredcorrect", 0);
            fb.setAttribute("data-numcorrect", num_correct);
            iDiv.append(fb);


        });
    }


            fetch("'''
    script_end='''")
      .then(response => response.json())
      .then(json => parse(json, '''
      #.then(json => console.log( '''

    script_end+=div_id
    script_end+= ''')
    );


    </script>
      '''
    javascript=script + url + script_end
    display(HTML(mydiv + javascript))

