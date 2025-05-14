from flask import Flask, request, jsonify, render_template
import json
import os
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize the room lights state
rooms = {
    "living_room": False,
    "sitting_room": False,
    "kitchen": False,
    "toilet": False,
    "bathroom": False,
    "bedroom": False
}

# Room name mapping for display purposes
room_display_names = {
    "living_room": "Living Room",
    "sitting_room": "Sitting Room",
    "kitchen": "Kitchen",
    "toilet": "Toilet",
    "bathroom": "Bathroom",
    "bedroom": "Bedroom"
}

@app.route('/')
def index():
    return render_template('index.html', rooms=rooms, room_display_names=room_display_names)

@app.route('/api/lights', methods=['POST'])
def update_lights():
    data = request.json
    print(f"Received data: {data}")
    # Get room and light state from request
    room = data.get('room', '').lower().replace(' ', '_')
    light_state = data.get('lights', False)
    # Update room state if it exists
    if room in rooms:
        rooms[room] = light_state
        # Emit a socket.io event to notify clients
        socketio.emit('light_state_change', {'room': room, 'lights': light_state})
        return jsonify({"success": True, "room": room, "lights": light_state})
    else:
        return jsonify({"success": False, "error": "Room not found"}), 404

@app.route('/api/get_states', methods=['GET'])
def get_states():
    return jsonify(rooms)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5004, debug=True, allow_unsafe_werkzeug=True)
