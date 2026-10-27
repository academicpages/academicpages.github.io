#!/usr/bin/env python3
import json
import re
from pathlib import Path


# Patch upstream _config.yml without touching any other byte.
config = Path('_config.yml').read_text(encoding='utf-8')
out = []
seen_title = False
seen_description = False
for line in config.splitlines(keepends=True):
    if re.match(r'^title\s*:', line):
        out.append('title: Orchard Sky OS-381 Volunteer Board\n')
        seen_title = True
    elif re.match(r'^description\s*:', line):
        out.append('description: Public volunteer assignments for the OS-381 stargazing night\n')
        out.append('email: crew@orchardsky.example\n')
        seen_description = True
    elif re.match(r'^email\s*:', line):
        out.append('email: crew@orchardsky.example\n')
    else:
        out.append(line)
if not seen_title or not seen_description:
    raise SystemExit('Expected unique title and description lines in _config.yml')
Path('_config.yml').write_text(''.join(out), encoding='utf-8')

about_lines = [
    '---',
    'title: "Orchard Sky OS-381 Volunteer Board"',
    'permalink: /',
    'layout: single',
    '---',
    '',
    '## Stargazing night',
    'Orchard Sky Public Stargazing Night',
    '',
    'Orchard Sky Collective publishes the volunteer roster.',
    '',
    '## Roster rule',
    'Roster rule: lead applications precede general applications; then use submission time and register occurrence.',
    '',
    '## Volunteer desk',
    'Volunteer desk: crew@orchardsky.example',
    '',
    '## Assignment result',
    'Four volunteers fill all four available places. Three valid applications are waitlisted and five application occurrences were rejected during validation.',
]
Path('_pages/about.md').write_text('\n'.join(about_lines) + '\n', encoding='utf-8')

application_keys = [
    'application_occurrence', 'application_id', 'volunteer_id', 'shift_id',
    'skill', 'service_tier', 'submitted_at', 'priority_position', 'status',
    'reason'
]
application_values = [
    (1, 'A1', 'VERA', 'LAWN', 'guide', 'general', '2055-08-09T08:00:00Z', 5, 'assigned', 'assigned'),
    (2, 'A2', 'OMAR', 'DOME', 'optics', 'lead', '2055-08-09T08:05:00Z', 1, 'assigned', 'assigned'),
    (3, 'A3', 'VERA', 'DOME', 'optics', 'lead', '2055-08-09T08:10:00Z', 2, 'waitlisted', 'shift-full'),
    (4, 'A4', 'NOAH', 'DESK', 'welcome', 'general', '2055-08-09T07:30:00Z', 4, 'assigned', 'assigned'),
    (5, 'A5', 'MIRA', 'LAWN', 'guide', 'general', '2055-08-09T08:20:00Z', 6, 'waitlisted', 'shift-full'),
    (6, 'A6', 'LINA', 'LAWN', 'guide', 'lead', '2055-08-09T08:15:00Z', 3, 'assigned', 'assigned'),
    (7, 'A7', 'OMAR', 'DESK', 'welcome', 'general', '2055-08-09T08:25:00Z', 7, 'waitlisted', 'volunteer-already-assigned'),
    (8, 'X1', 'IVY', 'LAWN', 'guide', 'lead', '2055-08-09T06:00:00Z', None, 'rejected', 'wrong-event'),
    (9, 'X2', 'PAX', 'DESK', 'welcome', 'general', '2055-08-09 09:00:00Z', None, 'rejected', 'invalid-application'),
    (10, 'X3', 'RHEA', 'STORE', 'inventory', 'lead', '2055-08-09T09:05:00Z', None, 'rejected', 'unknown-shift'),
    (11, 'X4', 'TARIQ', 'LAWN', 'optics', 'general', '2055-08-09T09:10:00Z', None, 'rejected', 'skill-mismatch'),
    (12, 'X5', 'UMA', 'DESK', 'welcome', 'general', '2055-08-09T18:00:01Z', None, 'rejected', 'after-cutoff'),
]
applications = [dict(zip(application_keys, values)) for values in application_values]

shift_keys = [
    'shift_id', 'shift_name', 'start_at', 'required_skill', 'capacity',
    'assigned_count', 'open_positions', 'assigned_volunteer_ids'
]
shift_values = [
    ('DESK', 'Welcome Desk', '2055-08-10T19:30:00Z', 'welcome', 1, 1, 0, ['NOAH']),
    ('DOME', 'Telescope Dome', '2055-08-10T20:00:00Z', 'optics', 1, 1, 0, ['OMAR']),
    ('LAWN', 'Constellation Lawn', '2055-08-10T20:30:00Z', 'guide', 2, 2, 0, ['LINA', 'VERA']),
]
shifts = [dict(zip(shift_keys, values)) for values in shift_values]

roster = {
    'event_id': 'OS-381',
    'event_name': 'Orchard Sky Public Stargazing Night',
    'cutoff_at': '2055-08-09T18:00:00Z',
    'application_occurrence_count': 12,
    'valid_application_count': 7,
    'rejected_application_count': 5,
    'eligible_shift_count': 3,
    'assigned_application_count': 4,
    'waitlisted_application_count': 3,
    'total_capacity': 4,
    'filled_positions': 4,
    'open_positions': 0,
    'application_audit': applications,
    'shift_roster': shifts,
}
Path('_data').mkdir(parents=True, exist_ok=True)
Path('_data/os-381-roster.json').write_text(
    json.dumps(roster, ensure_ascii=False, separators=(',', ':')) + '\n',
    encoding='utf-8')

header = 'application_occurrence,application_id,volunteer_id,shift_id,skill,service_tier,submitted_at,priority_position,status,reason'
csv_lines = [header]
for row in applications:
    csv_lines.append(','.join([
        str(row['application_occurrence']),
        row['application_id'],
        row['volunteer_id'],
        row['shift_id'],
        row['skill'],
        row['service_tier'],
        row['submitted_at'],
        '' if row['priority_position'] is None else str(row['priority_position']),
        row['status'],
        row['reason'],
    ]))
Path('downloads').mkdir(parents=True, exist_ok=True)
Path('downloads/os-381-application-audit.csv').write_text(
    '\n'.join(csv_lines) + '\n', encoding='utf-8')

board_lines = [
    '# OS-381 Volunteer Shift Board',
    '',
    'Event: Orchard Sky Public Stargazing Night',
    'Application cutoff: 2055-08-09T18:00:00Z',
    '',
    '| Priority | Application | Volunteer | Shift | Outcome |',
    '|---:|---|---|---|---|',
    '| 1 | A2 | OMAR | DOME | Assign |',
    '| 2 | A3 | VERA | DOME | Waitlist: shift full |',
    '| 3 | A6 | LINA | LAWN | Assign |',
    '| 4 | A4 | NOAH | DESK | Assign |',
    '| 5 | A1 | VERA | LAWN | Assign |',
    '| 6 | A5 | MIRA | LAWN | Waitlist: shift full |',
    '| 7 | A7 | OMAR | DESK | Waitlist: already assigned |',
    '',
    '| Shift | Start | Capacity | Assigned volunteers | Open |',
    '|---|---|---:|---|---:|',
    '| DESK | 2055-08-10T19:30:00Z | 1 | NOAH | 0 |',
    '| DOME | 2055-08-10T20:00:00Z | 1 | OMAR | 0 |',
    '| LAWN | 2055-08-10T20:30:00Z | 2 | LINA; VERA | 0 |',
    '',
    'Scope: 4 assigned; 3 waitlisted; 5 rejected; 12 total occurrences.',
    'Capacity: 4 of 4 places filled; 0 open.',
]
Path('downloads/os-381-shift-board.md').write_text(
    '\n'.join(board_lines) + '\n', encoding='utf-8')

print('OS-381 files written')
