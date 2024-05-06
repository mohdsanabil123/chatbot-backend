from flask import Flask, request, jsonify
import wikipedia

app = Flask(__name__)

@app.route('/', methods=['POST'])

def index():
    data = request.get_json()
    input_data = data['queryResult']['queryText']
    # print(data)
    # print(input_data)
    
    try:
        output_data = wikipedia.summary(input_data, sentences=1)
    except:
        output_data = "Sorry! Please search with different words."
    print(output_data)
    response = {
        'fulfillmentText': output_data
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False)