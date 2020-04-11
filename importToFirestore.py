import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('/Users/dylanduan/Downloads/flashcards-6cfa2-firebase-adminsdk-s14s9-3bf3fb08e6.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Define your flashcards
flashcards = [
    {"card": "AssemblyAI", "read": False},
    {"card": "Speech Recognition", "read": False},
    {"card": "Summarization", "read": False},
    {"card": "Moderation", "read": False},
    {"card": "Key Phrases", "read": False},
    {"card": "Speaker Labels", "read": False},
    {"card": "LeMUR", "read": False},
    {"card": "Auto-chapters", "read": False},
    {"card": "Entity Detection", "read": False},
    {"card": "Sentiment Analysis", "read": False},
    {"card": "Topic Detection", "read": False},
    {"card": "Audio Intelligence", "read": False},
    {"card": "API", "read": False},
    {"card": "Voice Data", "read": False},
    {"card": "Zendesk", "read": False},
    {"card": "Slack", "read": False},
    {"card": "Dylan Fox", "read": False},
    {"card": "Domenic Donato", "read": False},
    {"card": "Lee Vaughn", "read": False},
    {"card": "Andrew Galyan-Mann", "read": False},
    {"card": "Misra", "read": False},
    {"card": "cURL", "read": False},
    {"card": "Authorization", "read": False},
    {"card": "Transcription", "read": False},
    {"card": "AI Models", "read": False},
    {"card": "Insights", "read": False},
    {"card": "Language Support", "read": False},
    {"card": "Python", "read": False},
    {"card": "Java", "read": False},
    {"card": "Webhooks", "read": False},
    {"card": "Integration", "read": False},
    {"card": "SDK", "read": False},
    {"card": "Technology", "read": False},
    {"card": "Inference", "read": False},
    {"card": "Data Processing", "read": False},
    {"card": "OpenAI", "read": False},
    {"card": "Sam Altman", "read": False},
    {"card": "Machine Learning", "read": False},
    {"card": "Deep Learning", "read": False},
    {"card": "Artificial Intelligence", "read": False},
    {"card": "Neural Networks", "read": False},
    {"card": "Learning", "read": False},
    {"card": "Generate", "read": False},
    {"card": "Bias", "read": False},
    {"card": "Memory", "read": False},
    {"card": "Deepgram", "read": False},
    {"card": "Anthropic", "read": False},
    {"card": "Whisper", "read": False},
    {"card": "Looker", "read": False},
    {"card": "ZoomInfo", "read": False},
    {"card": "Salesforce", "read": False},
    {"card": "Sales Lead", "read": False},
    {"card": "Delete account", "read": False},
    {"card": "Veed", "read": False},
    {"card": "Spotify", "read": False},
    {"card": "Fireflies.ai", "read": False},
    {"card": "Treehouse", "read": False},
    {"card": "Solutions Architect", "read": False},
    {"card": "Marketing", "read": False},
    {"card": "People", "read": False},
    {"card": "Engineering", "read": False},
    {"card": "Deep Learning Research", "read": False},
    {"card": "SDR (Sales Development Representative)", "read": False},
    {"card": "Account Executive", "read": False},
    {"card": "Support Engineer", "read": False},
    {"card": "Frontend Engineer", "read": False},
    {"card": "Playground", "read": False},
    {"card": "Notion", "read": False},
    {"card": "S3 Bucket", "read": False},
    {"card": "Airtable", "read": False},
    {"card": "Playbook", "read": False},
    {"card": "Remote work", "read": False},
    {"card": "Github", "read": False},
    {"card": "Datadog", "read": False},
    {"card": "Papertrail", "read": False},
    {"card": "Posthog", "read": False},
    {"card": "Abbot", "read": False},
    {"card": "Discord", "read": False},
    {"card": "Asana", "read": False},
    {"card": "Status page", "read": False},
    {"card": "Outage", "read": False},
    {"card": "Server", "read": False},
    {"card": "GPU", "read": False},
    {"card": "All hands", "read": False},
    {"card": "Offsite", "read": False},
    {"card": "WeWork", "read": False},
    {"card": "Nano", "read": False},
    {"card": "Universal", "read": False},
    {"card": "Conformer 1", "read": False},
    {"card": "Conformer 2", "read": False},
    {"card": "Stack Overflow", "read": False},
    {"card": "Disfluencies", "read": False},
    {"card": "Claude", "read": False},
    {"card": "Sora", "read": False},
    {"card": "Gemini", "read": False},
    {"card": "Confidence Scores", "read": False},
    {"card": "Timestamps", "read": False},
    {"card": "Chat GPT", "read": False},
    {"card": "Research papers", "read": False},
    {"card": "Cookbook", "read": False},
    {"card": "Subtitles", "read": False},
    {"card": "Sentences", "read": False},
    {"card": "Paragraphs", "read": False},
    {"card": "Virtual meetings", "read": False},
    {"card": "Podcasts", "read": False},
    {"card": "Sales call", "read": False},
    {"card": "Custom text", "read": False},
    {"card": "Summary", "read": False},
    {"card": "Question and Answer", "read": False},
    {"card": "Task", "read": False},
    {"card": "Speakers expected", "read": False},
    {"card": "Speech threshold", "read": False},
    {"card": "Streaming", "read": False},
    {"card": "Real-time", "read": False},
    {"card": "Pull Request", "read": False},
    {"card": "Branch", "read": False},
    {"card": "Commit", "read": False},
    {"card": "Error", "read": False},
    {"card": "Bug", "read": False},
    {"card": "Jira", "read": False},
    {"card": "Customer Success", "read": False},
    {"card": "CLI", "read": False},
    {"card": "Timestamp", "read": False},
    {"card": "Concurrency", "read": False},
    {"card": "Encrypted", "read": False},
    {"card": "Discount", "read": False},
    {"card": "Analytics", "read": False},
    {"card": "Token", "read": False},
    {"card": "Upload", "read": False},
    {"card": "PII (Personal Identifiable Information)", "read": False}
]

# def delete_collection(coll_ref, batch_size):
#     docs = coll_ref.limit(batch_size).stream()
#     deleted = 0

#     for doc in docs:
#         print(f'Deleting doc {doc.id} => {doc.to_dict()}')
#         doc.reference.delete()
#         deleted = deleted + 1

#     if deleted >= batch_size:
#         return delete_collection(coll_ref, batch_size)

# # Usage example:
# db = firestore.client()
# delete_collection(db.collection(u'flashcards'), batch_size=123)


# Function to add a flashcard to Firestore
def add_flashcard(card):
    doc_ref = db.collection(u'flashcards').document()
    doc_ref.set(card)

# Populate Firestore with the flashcards
for flashcard in flashcards:
    add_flashcard(flashcard)

print("Finished populating Firestore with flashcards.")

# reset all flashcards to read=false

# db.collection("flashcards").get().then((snapshot) => {
#   snapshot.docs.forEach((doc) => {
#     db.collection("flashcards").doc(doc.id).update({ read: false })
#       .then(() => console.log(`Document ${doc.id} reset to read=false`))
#       .catch((error) => console.error("Error updating document:", error));
#   });
# });