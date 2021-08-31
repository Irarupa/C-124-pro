from flask import jsonify, Flask ,request 

app=Flask(__name__)

contact =[{'id': 1 , 'name': 'abc',  'contact': '1253'},{'id': 2 , 'name': 'cab',  'contact': '2153'} ]

@app.route('/get_contact')
def getTask():
    return jsonify({'data': contact})


@app.route('/add_contact', methods = ['POST'])
def addTask():
    if not request.json:
        return jsonify({'status': 'error', 'message': 'Please provide the contact'}, 400)

    c = {
        'id': contact[-1]['id']+1, 
        
    }    
    contact.append(c)
    return jsonify({'status': 'success', 'message': 'contact added successfully'},200)    




if __name__ == '__main__':
    app.run()
