import pandas as pd
from pandas import json_normalize
def transform_data(data):
    df=pd.DataFrame(data)
    for col in df.columns:
        df[col] = df[col].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
    return df



def transform_dynamic(df: pd.DataFrame):
    if df.empty:
        print("Empty DataFrame.")
        return None

    parent_data = []
    members_data = []
    milestones_data = []
    tech_data = []

    for row in df.to_dict(orient='records'):
        project_id = row.get('project_id') or f"project_{len(parent_data)+1}"

        # Extract client info safely
        client_info = row.get('client') or {}
        location = client_info.get('location') or {}
        team = row.get('team') or {}

        parent_data.append({
            'project_id': project_id,
            'project_name': row.get('project_name', ''),
            'client_name': client_info.get('name', ''),
            'client_industry': client_info.get('industry', ''),
            'client_city': location.get('city', ''),
            'client_country': location.get('country', ''),
            'status': row.get('status', ''),
            'project_manager': team.get('project_manager', '')
        })

        # Team members
        for member in team.get('members', []):
            if isinstance(member, dict):
                members_data.append({
                    'project_id': project_id,
                    'name': member.get('name', ''),
                    'role': member.get('role', '')
                })

        # Milestones
        for milestone in row.get('milestones', []):
            if isinstance(milestone, dict):
                milestones_data.append({
                    'project_id': project_id,
                    'milestone_name': milestone.get('name', ''),
                    'due_date': milestone.get('due_date', '')
                })

        # Technologies
        for tech in row.get('technologies', []):
            tech_data.append({
                'project_id': project_id,
                'technology': tech
            })

    # Convert to DataFrames
    df_project = pd.DataFrame(parent_data)
    df_members = pd.DataFrame(members_data)
    df_milestones = pd.DataFrame(milestones_data)
    df_technologies = pd.DataFrame(tech_data)

    return {
        'projects': df_project,
        'team_members': df_members,
        'milestones': df_milestones,
        'technologies': df_technologies
    }
