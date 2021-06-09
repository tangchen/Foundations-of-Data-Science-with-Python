function show_questions (json, mydiv) {
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
        iDiv.className='Quiz';
        mydiv.appendChild(iDiv);
        // iDiv.innerHTML=qa.question;

        // Create div to contain question part
        var qDiv = document.createElement('div');
        qDiv.id="quizQn"+id+index;
        qDiv.textContent=qa.question;
        iDiv.append(qDiv);

        // Create div to contain answer part
        var aDiv = document.createElement('div');
        aDiv.id="quizAns"+id+index;
        aDiv.className='Answer';
        iDiv.append(aDiv);

        console.log(qa.type);

        var num_correct;
        if (qa.type=="multiple_choice")  {
            num_correct=make_mc(qa, shuffle_answers, qDiv, aDiv, id);
        } else if   (qa.type=="many_choice"){
            num_correct=make_mc(qa, shuffle_answers, qDiv, aDiv, id);
        } else if  (qa.type=="numeric") {
            console.log("numeric");
            make_numeric(qa, qDiv, aDiv, id);
        }


        //Make div for feedback
        var fb = document.createElement("div");
        fb.id="fb"+id;
        //fb.style="font-size: 20px;text-align:center;";
        fb.className="Feedback";
        fb.setAttribute("data-answeredcorrect", 0);
        fb.setAttribute("data-numcorrect", num_correct);
        iDiv.append(fb);


    });
}