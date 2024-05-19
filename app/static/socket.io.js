<script>
        var socket = io.connect('http://' + document.domain + ':' + location.port);
        
        socket.on('connect', function() {
            socket.send('User has connected!');
        });

        socket.on('message', function(msg) {
            // 显示接收到的消息
            document.getElementById('your_chat_div').innerHTML += '<p>' + msg + '</p>';
        });
    </script>