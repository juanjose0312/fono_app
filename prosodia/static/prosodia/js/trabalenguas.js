let mediaRecorder; // Variable para almacenar el objeto MediaRecorder
let audioChunks = []; // Array para almacenar los fragmentos de audio grabados
let isRecording = false; // Variable para rastrear el estado de la grabación

function FuncionBoton(idbutton, idstatus, idresultado) {
    if (!isRecording) {
        // Iniciar grabación
        navigator.mediaDevices.getUserMedia({ audio: true }) // Solicitar acceso al micrófono
            .then(stream => {
                mediaRecorder = new MediaRecorder(stream); // Crear un nuevo MediaRecorder con el stream de audio
                mediaRecorder.start(); // Iniciar la grabación
                isRecording = true; // Actualizar el estado de grabación
                document.getElementById(idstatus).textContent = 'Grabando...'; // Actualizar el texto de estado
                document.getElementById(idbutton).textContent = 'Stop Recording'; // Cambiar el texto del botón

                mediaRecorder.addEventListener('dataavailable', event => {
                    audioChunks.push(event.data); // Añadir los fragmentos de audio grabados al array
                });

                mediaRecorder.addEventListener('stop', () => {
                    const audioBlob = new Blob(audioChunks, { type: 'audio/wav' }); // Crear un Blob con los fragmentos de audio
                    const formData = new FormData(); // Crear un nuevo FormData para enviar datos de formulario
                    formData.append('audio', audioBlob, 'grabacion.wav'); // Añadir el Blob de audio al FormData

                    // Enviar el FormData al servidor usando fetch
                    fetch('http://127.0.0.1:8000/prosodia/prosodia_trabalenguas/', {
                        method: 'POST', // Especificar el método HTTP como POST
                        headers: {
                            'X-CSRFToken': getCookie('csrftoken') // Incluir el token CSRF en los encabezados
                        },
                        body: formData // Establecer el cuerpo de la solicitud como el FormData que contiene el archivo de audio
                    })
                    .then(response => response.json()) // Convertir la respuesta del servidor a JSON
                    .then(data => {
                        document.getElementById(idresultado).textContent = `Resultado: ${data.result}`; // Mostrar el resultado del reconocimiento de voz en el elemento con id 'resultado'
                    })
                    .catch(error => console.error('Error:', error)); // Mostrar cualquier error que ocurra durante la solicitud en la consola

                    document.getElementById(idstatus).textContent = 'Grabación completa.'; // Actualizar el texto de estado
                    document.getElementById(idbutton).textContent = 'Start Recording'; // Cambiar el texto del botón
                    audioChunks = []; // Reiniciar el array de audioChunks para la próxima grabación
                });
            })
        .catch(error => {
            console.error('Error al acceder al micrófono:', error); // Mostrar cualquier error al acceder al micrófono en la consola
        });
    } 
    else{
        mediaRecorder.stop(); // Detener la grabación
        isRecording = false; // Actualizar el estado de grabación
        document.getElementById(idstatus).textContent = 'Grabación detenida'; // Actualizar el texto de estado
    }
};    

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.getElementById('recordButton_1').addEventListener('click', () => FuncionBoton("recordButton_1", "status_1", "resultado_1"));