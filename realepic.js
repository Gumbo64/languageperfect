interval = 500
dictionary = {};
function textbar(text){
    document.querySelector("#content-block > div.prompt-block > div").innerText = text;
}
setInterval(() => {
    question = document.querySelector("#question-text > span").innerText;
    try {
        answer = document.querySelector("#correct-answer-field").innerText;
    } catch (error) {
        answer = false;
    }
    
    if (!answer){
        if (!dictionary[question]){
            textbar('idk')
            
        }else{
            textbar('answer is: '+dictionary[question])
            console.log('answer is: '+dictionary[question])
        }
    }else{
        textbar('New answer found')
        dictionary[question]=document.querySelector("#correct-answer-field").innerText
    }
}, interval);
