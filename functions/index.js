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
exports.adminLogin = functions.https.onRequest(async (req, res) => {
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
  const cors = require('cors')({origin:true})
  exports.userLogin = functions.https.onRequest(async (req, res) => {
    cors(req,res, async() =>{
      /// Grab the text parameter.
      const original = req.query.text;
      // Push the new message into Firestore using the Firebase Admin SDK.
      var varsionList = ["auth","block"]
      let output = "ads";
      let count = 0


      for (let i = 0; i<varsionList.length; i++){
        const writeResult = await admin.firestore().collection(varsionList[i]);
        const snapshot = await writeResult.get();

        snapshot.forEach(doc => {
          console.log(original, doc.id)
          if(original == doc.id){
            count = 1
          }
        });
        
        if (count == 1) {
          output = "success"
        }
        else {
          output = "fail"
        }
      }
      
      console.log(output)
      // Send back a message that we've successfully written the message
      res.json({result: output});
    })
    
  });
  exports.getAccountData = functions.https.onRequest(async (req, res) => {
    cors(req,res, async() =>{
      const original = req.query.text;
      let last = original.split('|')
      let list = [];
      const writeResult = await admin.firestore().collection(last[0]).doc(last[1]).collection("keys");
      const snapshot = await writeResult.get();
      // console.log(snapshot)
      snapshot.forEach((doc) => {
        list.push(`${doc.id}`);
      });
      // Send back a message that we've successfully written the message
      res.json({result: list});
    })
  });


  exports.deletePC = functions.https.onRequest(async (req, res) => {
    cors(req,res, async() =>{
      const original = req.query.text;
      let output
      let last = original.split('|')
      try{
        const writeResult = await admin.firestore().collection(last[0]).doc(last[1]).collection("keys").doc(reqList[3]);
        writeResult.delete();
        output = "success"
      }catch(e){
        output = "fail"
      }
      
      res.json({result: list});
    })
  });
  exports.deleteAll = functions.https.onRequest(async (req, res) => {
    const original = req.query.text;
      let reqList = original.split('|')
      let list = [];
      const writeResult = await admin.firestore().collection(reqList[0]).doc(reqList[1]).collection("keys").doc(reqList[3]);
      const snapshot = await writeResult.get();
      // console.log(snapshot)
      snapshot.forEach((doc) => {
       //삭제 명령 넣을것
      });
      // Send back a message that we've successfully written the message
      res.json({result: list});
  });