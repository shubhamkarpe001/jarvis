$(document).ready(function () {
    // Initialize Textillate for text animations
    $('.text').text({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },
    });

    // Initialize SiriWave
    var SiriWaveInstant = new SiriWave({
        container: document.getElementById('siri-container'),
        style: 'ios9',
        speed: 0.30,
        amplitude: 2,
        width: 800,
        height: 200,
        autostart: true
    });

    SiriWaveInstant.start();  // Start the SiriWave animation

    // Define the object you want to display
    let myObject = {
        message: "HELLO J.A.R.V.I.S"
    };

    // Set the message content to the <p> element
    document.querySelector('.siri-message').innerText = myObject.message;

    $("#MicBtn").click(function () {
        // Hide the first section (Oval) and show the second section (SiriWave)
        $("#Oval").fadeOut();  // Hide the first section
        $("#SiriWaveInstant").fadeIn();  // Show the second section
        eel.allCommands()()
    });
    
function doc_keyUp(e){
    if (e.key === 'j' && e.metaKey){
        eel.PlayAssistantSound()
        $("#Oval").attr("hidden",true);
        $("#SiriWave").attr("hidden",false);
        eel.allCommands();

    }
}
    document.addEventListener('keyup',doc_keyUp,false);



    // to play assisatnt
    function PlayAssistant(message) {

        if (message != "") {

            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("")
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);

        }

    }

    // toogle fucntion to hide and display mic and send button 
    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
        else {
            $("#MicBtn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);
        }
    }


    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val();
        ShowHideButton(message)
    
    });
    
    // send button event handler
    $("#SendBtn").click(function () {
    
        let message = $("#chatbox").val()
        PlayAssistant(message)
    
    });


 // enter press event handler on chat box
 $("#chatbox").keypress(function (e) {
    key = e.which;
    if (key == 13) {
        let message = $("#chatbox").val()
        PlayAssistant(message)
    }
});
    
    
      
});
