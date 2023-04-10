/* eslint-disable */

// // Create and deploy your first functions
// // https://firebase.google.com/docs/functions/get-started
//
// exports.helloWorld = functions.https.onRequest((request, response) => {
//   functions.logger.info("Hello logs!", {structuredData: true});
//   response.send("Hello from Firebase!");
// });

// The Cloud Functions for Firebase SDK to create Cloud Functions and set up triggers.
const functions = require('firebase-functions');

// The Firebase Admin SDK to access Firestore.
const admin = require('firebase-admin');
admin.initializeApp();

// Take the text parameter passed to this HTTP endpoint and insert it into
// Firestore under the path /messages/:documentId/original
exports.addMessage = functions.https.onRequest(async (req, res) => {
    // Grab the text parameter.
    const original = req.query.text;
    // Push the new message into Firestore using the Firebase Admin SDK.
    const writeResult = await admin.firestore().collection('admin');
    const snapshot = await writeResult.get();
    let output = "ads";
    let id;

    let last = original.split('|')
    console.log(original )
    console.log(last)
    console.log(last[0])
    console.log(last[1])

    snapshot.forEach(doc => {
      if(last[0] == doc.data()['id']){
        id = doc
        return;
      }else{
        output ="IdError"
      }
    });
    try{
      if(last[0] == id.data()['id']){
        if(last[1] == id.data()['pw']){
          output = "success"
        }
        else{
          output ="dinied"
        }
      }
    }catch(exception) {
      console.log(exception);

    }
    
    console.log(output)
    // Send back a message that we've successfully written the message
    res.json({result: output});
  });