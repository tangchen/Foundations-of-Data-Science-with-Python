function check_numeric(event) {

    if (event.keyCode === 13) {
        this.blur();

        var id=this.id.split('-')[0];

        var submission=this.value;
        console.log("Reader entered", submission);


        console.log("In check_numeric(), id="+id);
        //console.log(event.srcElement.id)           
        //console.log(event.srcElement.dataset.correct)   
        //console.log(event.srcElement.dataset.feedback)

        var fb = document.getElementById("fb"+id);
        fb.style.display="none";
        fb.textContent="Incorrect";

        answers=JSON.parse(this.dataset.answers);
        console.log(answers);

        answers.forEach((answer,index,array) => {
            console.log(answer.type);

            correct=false;
            if (answer.type=="value"){
                if (submission == answer.value) {
                    fb.textContent=answer.feedback;
                    correct=answer.correct;
                    console.log(answer.correct);
                }
            } 

        }
                       );
        fb.style.display="block";
        if (correct) {
            this.style.background="#009113";
            fb.style.color="#009113";
        } else {
            this.style.background="#DC2329";
            fb.style.color="#DC2329";
        }



        return false;
    }

}

function make_numeric(qa, qDiv, aDiv, id) {



        //console.log(answer);

    
    qDiv.className="NumericQn";
    aDiv.style.display='block';

    var lab = document.createElement("label");
    lab.className="InpLabel";
    lab.textContent="Type numeric answer here:";
    aDiv.append(lab);

    var inp = document.createElement("input");
    inp.type="text";
    //inp.id="input-"+id;
    inp.id=id+"-0";
    inp.className="Input-text";
    inp.setAttribute('data-answers', JSON.stringify(qa.answers) );
    aDiv.append(inp);

    inp.addEventListener("keyup", check_numeric);

    /*
    inp.addEventListener("keyup", function(event) {
        if (event.keyCode === 13) {
            console.log(this.value);
            this.blur();
            return false;
        }
    }
                        );
    */



        // Make input element
    /*
        var inp = document.createElement("input");
        inp.type="radio";
        inp.id="quizo"+id+index;
        inp.style="display:none;";
        aDiv.append(inp);
        
        //Make label for input element
        var lab = document.createElement("label");
        lab.style="background: #fafafa; border: 1px solid #eee;  border-radius: 10px; padding: 10px; font-size: 16px; cursor: pointer; text-align: center;";
        lab.id=id+ '-' +index;
        lab.onclick=check_mc;
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

    */
    
}
