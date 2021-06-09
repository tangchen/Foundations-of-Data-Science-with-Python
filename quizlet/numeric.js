function check_numeric(ths, event) {

    if (event.keyCode === 13) {
        ths.blur();

        var id=ths.id.split('-')[0];

        var submission=ths.value;
				if (submission.indexOf('/') != -1) {
            sub_parts=submission.split('/');
            console.log(sub_parts);
            submission=sub_parts[0]/sub_parts[1];
        }
        console.log("Reader entered", submission);


        console.log("In check_numeric(), id="+id);
        //console.log(event.srcElement.id)           
        //console.log(event.srcElement.dataset.correct)   
        //console.log(event.srcElement.dataset.feedback)

        var fb = document.getElementById("fb"+id);
        fb.style.display="none";
        fb.textContent="Incorrect -- try again.";

        answers=JSON.parse(ths.dataset.answers);
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
            //ths.style.background="#009113";
            //fb.style.color="#009113";
            ths.className="Input-text";
            ths.classList.add("correctButton");
            fb.className="Feedback";
            fb.classList.add("correct");
        } else {
            //ths.style.background="#DC2329";
            //fb.style.color="#DC2329";
            ths.className="Input-text";
            ths.classList.add("incorrectButton");
            fb.className="Feedback";
            fb.classList.add("incorrect");
        }



        return false;
    }

}

function isValid(el,  charC) {
		if (charC == 46) {
				if (el.value.indexOf('.') === -1) {
					  return true;
				} else if (el.value.indexOf('/') != -1) {
            parts=el.value.split('/');
				    if (parts[1].indexOf('.') === -1) {
					      return true;
            }
        }
        else{
					  return false;
				}
		} else if (charC == 47) {
				if (el.value.indexOf('/') === -1) {
            if ((el.value != "") && (el.value != ".")) {
					      return true;
            } else {
					  return false;
				    }
        } else {
            return false;
        }
		} else {
				if (charC > 31 && (charC < 48 || charC > 57))
					  return false;
		}
		return true;
}

function numeric_keypress( evnt) {
		var charC = (evnt.which) ? evnt.which : evnt.keyCode;

    if (charC==13) {
        check_numeric(this, evnt);
    } else{
		    return isValid(this, charC);
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
    console.log(inp);

    //inp.addEventListener("keypress", check_numeric);
    //inp.addEventListener("keypress", numeric_keypress);
    /*
    inp.addEventListener("keypress", function(event) {
        return numeric_keypress(this, event);
    }
                        );
                        */
    //inp.onkeypress="return numeric_keypress(this, event)";
    inp.onkeypress=numeric_keypress;
    inp.onpaste= event => false;

    inp.addEventListener("focus", function(event) {
        this.value="";
        return false;
    }
                        );


}
