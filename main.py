from event import Event
import datetime 

if __name__ == "__main__":
    event1 = Event("Birthday Party", "2024-05-20")

    event1.add_participant()
    event1.add_participant()
    event1.add_participant()

    participant_count = event1.get_participant_count()

    print(f"Participant count for {event1.name}: {participant_count}")