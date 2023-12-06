import csv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred = credentials.Certificate("just-test-tutorials-firebase-adminsdk-jt9n3-5af427c0c9.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# for i in range(1,3):
#     doc_ref = db.collection("auth").document('asdfef').collections('keys').document(i)
#     doc_ref.set({
#             u'keyCount': 1,
#             u'owner' : 1,
#             u'purpose': 1,
#             u'note': 1,
#         })


collections =  db.collection("auth").document("asdfef").collections()
for collection in collections:
    for doc in collection.stream():
        db.collection("auth").document("asdfef").collection('keys').document(doc.id).delete()