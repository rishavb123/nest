console.log("HELLO FROM THE EXTENSION");

const config = {
    apiKey: "AIzaSyCGWN5N689bcT4m0ceBKwrAs2n2XG2CK_A",
    authDomain: "nest-controller.firebaseapp.com",
    databaseURL: "https://nest-controller.firebaseio.com",
    projectId: "nest-controller",
    storageBucket: "nest-controller.appspot.com",
    messagingSenderId: "934756714072"
};
firebase.initializeApp(config);

firebase.database().ref("test").on("value", snap => {
    console.log(snap.val());
});

let dbCurrentTemp = 0;
let dbSetTemp = 0;

firebase.database().ref("CurrentTemp").on("value", snap => {
    dbCurrentTemp = snap.val();
});

firebase.database().ref("SetTemp").on("value", snap => {
    dbSetTemp = snap.val();
});

function app()
{
    let wrapper = document.getElementsByClassName('temperature-container')[0]
    let span = wrapper.getElementsByTagName('span')[0];
    let curTemp = parseInt(span.innerHTML);
    if(dbCurrentTemp != curTemp)
        firebase.database().ref("CurrentTemp").set(curTemp);
    if(curTemp != dbSetTemp)
    {
        if(curTemp < dbSetTemp)
        {
            up();
        }
        else
        {
            down();
        }
    }
    setTimeout(app, 3000);
}

function up()
{
    let wrapper = document.getElementsByClassName('control-container')[0];
    let upBtn = wrapper.getElementsByClassName('up-control')[0];
    upBtn.click();
}

function down()
{
    let wrapper = document.getElementsByClassName('control-container')[0];
    let downBtn = wrapper.getElementsByClassName('down-control')[0];
    downBtn.click();
}

window.addEventListener("keypress", e => {
    if(e.keyCode == 32)
    {
        alert("Starting . . .");
        setTimeout(app, 100);
    }
});
