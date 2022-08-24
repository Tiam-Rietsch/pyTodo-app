
let progressBar = document.querySelectorAll(".circular-progress");
let progressValue = document.querySelectorAll(".progress-value");

for (let i=0; i < progressBar.length; i++) {
    let value = 0;
    let endValue =parseInt(progressValue[i].textContent);
    let speed = 20;    
    
    let barProgress = setInterval(() => {
        if (value == endValue) {
            clearInterval(barProgress);
        } else {
            value ++;
        }
        let degVal = value * 3.6;
        progressValue[i].textContent = value.toString() + "%";
        if (value == 100) {
            progressBar[i].style.background =  "conic-gradient(#2AD352 " + degVal.toString() + "deg , #dce0e4  0deg)";
        } else if (value == endValue) {
            progressBar[i].style.background =  "conic-gradient(#5A69C9 " + degVal.toString() + "deg , #dce0e4  0deg)";
        } else {
            progressBar[i].style.background =  "conic-gradient(#343A40 " + degVal.toString() + "deg , #dce0e4  0deg)";
        }
        if (value == endValue) {
            clearInterval(barProgress);
        }    
        
    
    }, speed);
}
