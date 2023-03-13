from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")

@app.route('/xTrans/<value>')
def xTrans(value): 
    app.config["kinematics"].x_trans = float(value)
    app.config["kinematics"].apply_transition()
    return jsonify("x-Translation")

@app.route('/yTrans/<value>')
def yTrans(value):
    app.config["kinematics"].y_trans = float(value)
    app.config["kinematics"].apply_transition()
    return jsonify("y-Translation")

@app.route('/zTrans/<value>')
def zTrans(value):
    app.config["kinematics"].z_trans = float(value)
    app.config["kinematics"].apply_transition()
    return jsonify("z-Translation")

@app.route('/xRot/<value>')
def xRot(value):
    app.config["kinematics"].x_rot = float(value)
    app.config["kinematics"].apply_transition()
    return jsonify("x-Rotation")

@app.route('/yRot/<value>')
def yRot(value):
    app.config["kinematics"].y_rot = float(value)
    app.config["kinematics"].apply_transition()
    return jsonify("y-Rotation")

@app.route('/zRot/<value>')
def zRot(value):
    app.config["kinematics"].z_rot = float(value)
    app.config["kinematics"].apply_transition()
    return jsonify("z-Rotation")

@app.route('/reset')
def reset():
    app.config["kinematics"].x_trans = 0
    app.config["kinematics"].y_trans = 0
    app.config["kinematics"].z_trans = 25
    app.config["kinematics"].x_rot   = 0
    app.config["kinematics"].y_rot   = 0
    app.config["kinematics"].z_rot   = 0
    app.config["kinematics"].apply_transition()
    return jsonify("resetting ...")

@app.route('/setValues')
def set_value():
    x_trans = app.config["kinematics"].x_trans
    y_trans = app.config["kinematics"].y_trans
    z_trans = app.config["kinematics"].z_trans
    x_rot   = app.config["kinematics"].x_rot
    y_rot   = app.config["kinematics"].y_rot
    z_rot   = app.config["kinematics"].z_rot

    defaultVals = [x_trans, y_trans, z_trans, x_rot, y_rot, z_rot]
    return jsonify(defaultVals)

def create_app(kinematics):
    app.config["kinematics"] = kinematics;
    return app

#if __name__ == '__main__':
#    app.run()
