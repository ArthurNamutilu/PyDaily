attendants = {'Arthur': 'present', 'Fred': 'present', 'Gg': 'absent', 'Erickson': 'absent', 'Dela': 'inactive'}

# copy() - creates new {} copy of original {} -avoid modifying while iterating
for attendee, status in attendants.copy().items():
    if status == 'absent':
        del attendants[attendee]

active = {}
for attendee, status in attendants.items():
    if status == 'present':
        active[attendee] = status
print(attendants)
print(f"Available rn {active}")
