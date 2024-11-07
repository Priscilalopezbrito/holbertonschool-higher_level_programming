import os
'''
Creating a Simple Templating Program
'''


def generate_invitations(template, attendees):
    #  Check Input Types:
    if not isinstance(template, str):
        print('Error: Template must be a string.')
        return

    if not isinstance(attendees, list):
        print('Error: Attendees must be a list of dictionaries.')
        return

    # Handle Empty Inputs:
    if not template.strip():
        print('Template is empty, no output files generated.')
        return
    if not attendees:
        print('No data provided, no output files generated.')
        return

    # Process Each Attendee:
    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key, 'N/A')
            invitation = (
                invitation.replace(f'{{{key}}}', value if value else 'N/A')
            )

        # Generate Output Files:
        output_filename = f'output_{index}.txt'
        if os.path.exists(output_filename):
            print(f"Warning: {output_filename} already exists.")
            continue
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(invitation)
            print(f"Invitation generated: {output_filename}")
        except IOError as e:
            print(f"Error writing to file {output_filename}: {e}")
