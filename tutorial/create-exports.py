import json
import requests
import datetime
import auth

base_url = 'https://enterprise.onna.com'
oauth_path = '/auth/oauth/'
username = "stefano@oscillator.es"
container = "stefanoonnanov2020"
account = "stefanoonnanov2020"
password = "iLuFJuYSGYQ58r3*"
path = "https://enterprise.onna.com/stefanoonnanov2020/user/workspaces/demo-obYwIS"

# Y0urP#ssWoRD! is your super-secret account password
# CONTAINER is the name of your Onna account. For more info see https://developers.onna.com/glossary.html#container
# MYACCOUNT is the name of your Onna account
# USERNAME is the email you signed up with
# PATH is the URL of your Datasource. For example {baseurl}/{account}/user/workspaces/demo-obYwIS

resp = requests.get(f'{base_url}/api/{container}/{account}/@oauthgetcode?client_id=canonical&scope={account}')
auth_code = resp.json()['auth_code']
print(f"auth_code: {auth_code}")

payload = {'grant_type': "user",
           'code': auth_code,
           'username': f"{username}",
           'password': f"{password}",
           'scopes': [f"{account}"],
           'client_id': "canonical"
          }
headers = {'Accept': 'application/json'}
resp = requests.post(f'{base_url}/{oauth_path}/get_auth_token', headers=headers, data=json.dumps(payload))
jwt_token = resp.text
print(f"jwt_token: {jwt_token}")

def export_past_week(path, username, account, container):
    today = datetime.date.today()
    seven_days_ago = today + datetime.timedelta(days=-8)
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt_token()}'}
    export_name = f"Export-PastWeek-{today}"

# POST request to create export
    url = f'{base_url}/api/{container}/{account}/{username}'
    payload = {
            "title": f"{export_name}",
            "settings": [
                {
                    "exclude_nist": True,
                    "include_family": True,
                    "dedupe_parents": False,
                    "prefer_pdf": False,
                    "message_context_days": 0,
                    "slack_as_single_message": True,
                    "meta": {
                        "onna.canonical.content.resource.IResource": [
                            {
                                "selected": False,
                                "viewValue": "Title",
                                "value": "title"
                            }
                        ],
                        "guillotina.behaviors.dublincore.IDublinCore": [
                            {
                                "selected": False,
                                "viewValue": "Expiration date",
                                "value": "expiration_date"
                            },
                            {
                                "selected": False,
                                "viewValue": "Description",
                                "value": "description"
                            },
                            {
                                "selected": False,
                                "viewValue": "Effective date",
                                "value": "effective_date"
                            },
                            {
                                "selected": False,
                                "viewValue": "Tags",
                                "value": "tags"
                            }
                        ],
                        "guillotina.behaviors.dynamic.IDynamicFieldValues": [
                            {
                                "viewValue": "Custom fields",
                                "value": "values",
                                "selected": False
                            }
                        ],
                        "onna.canonical.behaviors.contract.IContract": [
                            {
                                "selected": False,
                                "viewValue": "Deal summary",
                                "value": "deal_summary"
                            },
                            {
                                "selected": False,
                                "viewValue": "Term type",
                                "value": "term_type"
                            },
                            {
                                "selected": False,
                                "viewValue": "Contract requestor",
                                "value": "contract_requestor"
                            },
                            {
                                "selected": False,
                                "viewValue": "Notification frequency",
                                "value": "notification_frequency"
                            },
                            {
                                "selected": False,
                                "viewValue": "First expiration notification",
                                "value": "first_expiration_notification"
                            },
                            {
                                "selected": False,
                                "viewValue": "Approvers",
                                "value": "approvers_and_signatories"
                            },
                            {
                                "selected": False,
                                "viewValue": "External party",
                                "value": "external_party"
                            },
                            {
                                "selected": False,
                                "viewValue": "Subscribers",
                                "value": "subscribers"
                            },
                            {
                                "selected": False,
                                "viewValue": "Master agreement",
                                "value": "master_agreement"
                            },
                            {
                                "selected": False,
                                "viewValue": "Hierarchy type",
                                "value": "hierarchy_type"
                            },
                            {
                                "selected": False,
                                "viewValue": "Renewed version",
                                "value": "renewed_version"
                            },
                            {
                                "selected": False,
                                "viewValue": "Amount",
                                "value": "amount"
                            },
                            {
                                "selected": False,
                                "viewValue": "Comments",
                                "value": "comments"
                            },
                            {
                                "selected": False,
                                "viewValue": "Legacy contract number",
                                "value": "legacy_contract_number"
                            },
                            {
                                "selected": False,
                                "viewValue": "First renewal notification",
                                "value": "first_renewal_notification"
                            },
                            {
                                "selected": False,
                                "viewValue": "Engagement type",
                                "value": "engagement_type"
                            },
                            {
                                "selected": False,
                                "viewValue": "Manager expiration notification",
                                "value": "manager_expiration_notification"
                            },
                            {
                                "selected": False,
                                "viewValue": "Legal approver",
                                "value": "legal_approver"
                            },
                            {
                                "selected": False,
                                "viewValue": "Clean contract",
                                "value": "clean_contract"
                            },
                            {
                                "selected": False,
                                "viewValue": "Includes privacy data",
                                "value": "includes_privacy_data"
                            },
                            {
                                "selected": False,
                                "viewValue": "Contract number",
                                "value": "contract_number"
                            },
                            {
                                "selected": False,
                                "viewValue": "Contract type",
                                "value": "contract_type"
                            },
                            {
                                "selected": False,
                                "viewValue": "Amount currency",
                                "value": "amount_currency"
                            },
                            {
                                "selected": False,
                                "viewValue": "Contract requested",
                                "value": "contract_requested"
                            },
                            {
                                "selected": False,
                                "viewValue": "Contract status",
                                "value": "contract_status"
                            },
                            {
                                "selected": False,
                                "viewValue": "Legal entity",
                                "value": "legal_entity"
                            },
                            {
                                "selected": False,
                                "viewValue": "Contract origin",
                                "value": "contract_origin"
                            },
                            {
                                "selected": False,
                                "viewValue": "Preparer",
                                "value": "preparer"
                            },
                            {
                                "selected": False,
                                "viewValue": "Contract subtype",
                                "value": "contract_subtype"
                            },
                            {
                                "selected": False,
                                "viewValue": "Departments",
                                "value": "departments"
                            },
                            {
                                "selected": False,
                                "viewValue": "Contract owner",
                                "value": "contract_owner"
                            }
                        ],
                        "onna.canonical.behaviors.conversation.IConversation": [
                            {
                                "selected": False,
                                "viewValue": "Conversation ID",
                                "value": "thread_id"
                            },
                            {
                                "selected": False,
                                "viewValue": "Conversation name",
                                "value": "thread_name"
                            },
                            {
                                "selected": False,
                                "viewValue": "Conversation type",
                                "value": "thread_type"
                            }
                        ],
                        "onna.canonical.behaviors.folderdata.IFolderData": [
                            {
                                "selected": False,
                                "viewValue": "Revision",
                                "value": "revision"
                            },
                            {
                                "selected": False,
                                "viewValue": "Parent folder",
                                "value": "parent_folder"
                            },
                            {
                                "selected": False,
                                "viewValue": "Path to original file",
                                "value": "orig_path"
                            }
                        ],
                        "onna.canonical.behaviors.origin.IOrigin": [
                            {
                                "viewValue": "List of creators in source",
                                "value": "origin_created_by",
                                "selected": True
                            },
                            {
                                "viewValue": "URL to original file",
                                "value": "origin",
                                "selected": True
                            },
                            {
                                "viewValue": "List of modifiers in source",
                                "value": "origin_modified_by",
                                "selected": True
                            },
                            {
                                "viewValue": "List of users collected for",
                                "value": "origin_targeted_users",
                                "selected": True
                            },
                            {
                                "viewValue": "Other source metadata",
                                "value": "origin_other_metadata",
                                "selected": True
                            },
                            {
                                "viewValue": "Last modified in source",
                                "value": "origin_server_modified",
                                "selected": True
                            },
                            {
                                "viewValue": "Exception",
                                "value": "origin_exception",
                                "selected": True
                            },
                            {
                                "viewValue": "Synced folder or label in source",
                                "value": "filter",
                                "selected": True
                            },
                            {
                                "viewValue": "Synced folder or label ID in source",
                                "value": "origin_label_ids",
                                "selected": True
                            }
                        ],
                        "onna.canonical.behaviors.machine_learning.IMachineLearning": [
                            {
                                "viewValue": "NIST file",
                                "value": "nist",
                                "selected": False
                            },
                            {
                                "viewValue": "Detected language",
                                "value": "language",
                                "selected": False
                            }
                        ],
                        "onna.canonical.content.resources.confluence.IConfluence": [
                            {
                                "selected": False,
                                "viewValue": "Ancestors of file",
                                "value": "ancestors"
                            },
                            {
                                "selected": False,
                                "viewValue": "Space type",
                                "value": "space_type"
                            },
                            {
                                "selected": False,
                                "viewValue": "Space ID",
                                "value": "space"
                            },
                            {
                                "selected": False,
                                "viewValue": "Space name",
                                "value": "space_name"
                            },
                            {
                                "selected": False,
                                "viewValue": "Labels",
                                "value": "confluence_labels"
                            }
                        ],
                        "onna.canonical.content.resources.jira.IJira": [
                            {
                                "selected": False,
                                "viewValue": "Project key",
                                "value": "thread_id"
                            },
                            {
                                "selected": False,
                                "viewValue": "Project name",
                                "value": "thread_name"
                            },
                            {
                                "selected": False,
                                "viewValue": "Project type",
                                "value": "thread_type"
                            }
                        ],
                        "onna.canonical.content.resources.mail.IMail": [
                            {
                                "selected": False,
                                "viewValue": "Email subject",
                                "value": "subject"
                            },
                            {
                                "selected": False,
                                "viewValue": "Email to",
                                "value": "to_mail"
                            },
                            {
                                "selected": False,
                                "viewValue": "Email from",
                                "value": "from_mail"
                            },
                            {
                                "selected": False,
                                "viewValue": "Starred",
                                "value": "is_starred"
                            },
                            {
                                "selected": False,
                                "viewValue": "Email Bcc",
                                "value": "bcc_mail"
                            },
                            {
                                "selected": False,
                                "viewValue": "Email Cc",
                                "value": "cc_mail"
                            },
                            {
                                "selected": False,
                                "viewValue": "Important",
                                "value": "is_important"
                            },
                            {
                                "selected": False,
                                "viewValue": "Email ID",
                                "value": "message_id"
                            }
                        ],
                        "onna.canonical.content.resources.eslack.IESlack": [
                            {
                                "selected": True,
                                "viewValue": "Workspace ID",
                                "value": "workspace_id"
                            },
                            {
                                "selected": True,
                                "viewValue": "Workspace name",
                                "value": "workspace_name"
                            }
                        ],
                        "onna.canonical.content.resources.zendesk.IZendesk": [
                            {
                                "selected": False,
                                "viewValue": "Ticket name",
                                "value": "thread_name"
                            },
                            {
                                "selected": False,
                                "viewValue": "Ticket requester",
                                "value": "requester"
                            },
                            {
                                "selected": False,
                                "viewValue": "Ticket status",
                                "value": "status"
                            },
                            {
                                "selected": False,
                                "viewValue": "Ticket ID",
                                "value": "thread_id"
                            },
                            {
                                "selected": False,
                                "viewValue": "Tags",
                                "value": "tags"
                            },
                            {
                                "selected": False,
                                "viewValue": "Group membership",
                                "value": "group"
                            },
                            {
                                "selected": False,
                                "viewValue": "Ticket priority",
                                "value": "priority"
                            },
                            {
                                "selected": False,
                                "viewValue": "Ticket type",
                                "value": "thread_type"
                            },
                            {
                                "selected": False,
                                "viewValue": "Organization",
                                "value": "organization"
                            },
                            {
                                "selected": False,
                                "viewValue": "Ticket responsible",
                                "value": "assignee"
                            }
                        ],
                        "onna.canonical.content.resources.workplace.IWorkplace": [
                            {
                                "selected": False,
                                "viewValue": "Workplace conversation ID",
                                "value": "thread_id"
                            },
                            {
                                "selected": False,
                                "viewValue": "Workplace conversation name",
                                "value": "thread_name"
                            },
                            {
                                "selected": False,
                                "viewValue": "Workplace conversation type",
                                "value": "thread_type"
                            }
                        ],
                        "onna.canonical.behaviors.metadata.IMetadata": [
                            {
                                "viewValue": "Content type",
                                "value": "content_type",
                                "selected": True
                            },
                            {
                                "viewValue": "File name",
                                "value": "resource_name",
                                "selected": True
                            },
                            {
                                "viewValue": "Author",
                                "value": "author",
                                "selected": True
                            },
                            {
                                "viewValue": "File size",
                                "value": "content_length",
                                "selected": True
                            },
                            {
                                "viewValue": "Company",
                                "value": "company",
                                "selected": True
                            },
                            {
                                "viewValue": "File title",
                                "value": "processing_title",
                                "selected": True
                            },
                            {
                                "viewValue": "MD5 hash",
                                "value": "md5",
                                "selected": True
                            },
                            {
                                "viewValue": "File last modified",
                                "value": "date_modified",
                                "selected": True
                            },
                            {
                                "viewValue": "Other document metadata",
                                "value": "other_metadata",
                                "selected": True
                            },
                            {
                                "viewValue": "Application name",
                                "value": "application_name",
                                "selected": True
                            },
                            {
                                "viewValue": "Processing exception",
                                "value": "processing_exception",
                                "selected": True
                            },
                            {
                                "viewValue": "File creation",
                                "value": "date_created",
                                "selected": True
                            },
                            {
                                "viewValue": "Extension",
                                "value": "extension",
                                "selected": True
                            }
                        ],
                        "onna.canonical.behaviors.related_users.IRelatedUsers": [
                            {
                                "selected": False,
                                "viewValue": "List of related users",
                                "value": "related_users"
                            }
                        ],
                        "onna.canonical.behaviors.xtag.IXTag": [
                            {
                                "selected": False,
                                "viewValue": "List of XTags",
                                "value": "tags"
                            }
                        ]
                    },
                    "formattedMeta": [
                        {
                            "label": "Confluence",
                            "children": [
                                {
                                    "label": "Ancestors of file",
                                    "value": "onna.canonical.content.resources.confluence.IConfluence|ancestors",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Labels",
                                    "value": "onna.canonical.content.resources.confluence.IConfluence|confluence_labels",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Space ID",
                                    "value": "onna.canonical.content.resources.confluence.IConfluence|space",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Space name",
                                    "value": "onna.canonical.content.resources.confluence.IConfluence|space_name",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Space type",
                                    "value": "onna.canonical.content.resources.confluence.IConfluence|space_type",
                                    "isSelected": False,
                                    "isHidden": True
                                }
                            ]
                        },
                        {
                            "label": "Contract",
                            "children": [
                                {
                                    "label": "Amount",
                                    "value": "onna.canonical.behaviors.contract.IContract|amount",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Amount currency",
                                    "value": "onna.canonical.behaviors.contract.IContract|amount_currency",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Approvers",
                                    "value": "onna.canonical.behaviors.contract.IContract|approvers_and_signatories",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Clean contract",
                                    "value": "onna.canonical.behaviors.contract.IContract|clean_contract",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Comments",
                                    "value": "onna.canonical.behaviors.contract.IContract|comments",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Contract number",
                                    "value": "onna.canonical.behaviors.contract.IContract|contract_number",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Contract origin",
                                    "value": "onna.canonical.behaviors.contract.IContract|contract_origin",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Contract owner",
                                    "value": "onna.canonical.behaviors.contract.IContract|contract_owner",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Contract requested",
                                    "value": "onna.canonical.behaviors.contract.IContract|contract_requested",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Contract requestor",
                                    "value": "onna.canonical.behaviors.contract.IContract|contract_requestor",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Contract status",
                                    "value": "onna.canonical.behaviors.contract.IContract|contract_status",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Contract subtype",
                                    "value": "onna.canonical.behaviors.contract.IContract|contract_subtype",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Contract type",
                                    "value": "onna.canonical.behaviors.contract.IContract|contract_type",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Deal summary",
                                    "value": "onna.canonical.behaviors.contract.IContract|deal_summary",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Departments",
                                    "value": "onna.canonical.behaviors.contract.IContract|departments",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Engagement type",
                                    "value": "onna.canonical.behaviors.contract.IContract|engagement_type",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "External party",
                                    "value": "onna.canonical.behaviors.contract.IContract|external_party",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "First expiration notification",
                                    "value": "onna.canonical.behaviors.contract.IContract|first_expiration_notification",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "First renewal notification",
                                    "value": "onna.canonical.behaviors.contract.IContract|first_renewal_notification",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Hierarchy type",
                                    "value": "onna.canonical.behaviors.contract.IContract|hierarchy_type",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Includes privacy data",
                                    "value": "onna.canonical.behaviors.contract.IContract|includes_privacy_data",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Legacy contract number",
                                    "value": "onna.canonical.behaviors.contract.IContract|legacy_contract_number",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Legal approver",
                                    "value": "onna.canonical.behaviors.contract.IContract|legal_approver",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Legal entity",
                                    "value": "onna.canonical.behaviors.contract.IContract|legal_entity",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Manager expiration notification",
                                    "value": "onna.canonical.behaviors.contract.IContract|manager_expiration_notification",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Master agreement",
                                    "value": "onna.canonical.behaviors.contract.IContract|master_agreement",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Notification frequency",
                                    "value": "onna.canonical.behaviors.contract.IContract|notification_frequency",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Preparer",
                                    "value": "onna.canonical.behaviors.contract.IContract|preparer",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Renewed version",
                                    "value": "onna.canonical.behaviors.contract.IContract|renewed_version",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Subscribers",
                                    "value": "onna.canonical.behaviors.contract.IContract|subscribers",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Term type",
                                    "value": "onna.canonical.behaviors.contract.IContract|term_type",
                                    "isSelected": False,
                                    "isHidden": True
                                }
                            ]
                        },
                        {
                            "label": "Conversation (Slack, Hangouts)",
                            "children": [
                                {
                                    "label": "Conversation ID",
                                    "value": "onna.canonical.behaviors.conversation.IConversation|thread_id",
                                    "isSelected": True,
                                    "isHidden": True
                                },
                                {
                                    "label": "Conversation name",
                                    "value": "onna.canonical.behaviors.conversation.IConversation|thread_name",
                                    "isSelected": True,
                                    "isHidden": True
                                },
                                {
                                    "label": "Conversation type",
                                    "value": "onna.canonical.behaviors.conversation.IConversation|thread_type",
                                    "isSelected": True,
                                    "isHidden": True
                                }
                            ]
                        },
                        {
                            "label": "Email (Gmail, IMAP, MS Outlook)",
                            "children": [
                                {
                                    "label": "Email Bcc",
                                    "value": "onna.canonical.content.resources.mail.IMail|bcc_mail",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Email Cc",
                                    "value": "onna.canonical.content.resources.mail.IMail|cc_mail",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Email from",
                                    "value": "onna.canonical.content.resources.mail.IMail|from_mail",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Email ID",
                                    "value": "onna.canonical.content.resources.mail.IMail|message_id",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Email subject",
                                    "value": "onna.canonical.content.resources.mail.IMail|subject",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Email to",
                                    "value": "onna.canonical.content.resources.mail.IMail|to_mail",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Important",
                                    "value": "onna.canonical.content.resources.mail.IMail|is_important",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Starred",
                                    "value": "onna.canonical.content.resources.mail.IMail|is_starred",
                                    "isSelected": False,
                                    "isHidden": True
                                }
                            ]
                        },
                        {
                            "label": "File data",
                            "children": [
                                {
                                    "label": "Description",
                                    "value": "guillotina.behaviors.dublincore.IDublinCore|description",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Effective date",
                                    "value": "guillotina.behaviors.dublincore.IDublinCore|effective_date",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Expiration date",
                                    "value": "guillotina.behaviors.dublincore.IDublinCore|expiration_date",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Tags",
                                    "value": "guillotina.behaviors.dublincore.IDublinCore|tags",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Title",
                                    "value": "onna.canonical.content.resource.IResource|title",
                                    "isSelected": False,
                                    "isHidden": True
                                }
                            ]
                        },
                        {
                            "label": "Folder data",
                            "children": [
                                {
                                    "label": "Parent folder",
                                    "value": "onna.canonical.behaviors.folderdata.IFolderData|parent_folder",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Path to original file",
                                    "value": "onna.canonical.behaviors.folderdata.IFolderData|orig_path",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Revision",
                                    "value": "onna.canonical.behaviors.folderdata.IFolderData|revision",
                                    "isSelected": False,
                                    "isHidden": True
                                }
                            ]
                        },
                        {
                            "label": "Jira",
                            "children": [
                                {
                                    "label": "Project key",
                                    "value": "onna.canonical.content.resources.jira.IJira|thread_id",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Project name",
                                    "value": "onna.canonical.content.resources.jira.IJira|thread_name",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Project type",
                                    "value": "onna.canonical.content.resources.jira.IJira|thread_type",
                                    "isSelected": False,
                                    "isHidden": True
                                }
                            ]
                        },
                        {
                            "label": "RelatedUsers",
                            "children": [
                                {
                                    "label": "List of related users",
                                    "value": "onna.canonical.behaviors.related_users.IRelatedUsers|related_users",
                                    "isSelected": True,
                                    "isHidden": True
                                }
                            ]
                        },
                        {
                            "label": "Slack Enterprise",
                            "children": [
                                {
                                    "label": "Workspace ID",
                                    "value": "onna.canonical.content.resources.eslack.IESlack|workspace_id",
                                    "isSelected": True,
                                    "isHidden": True
                                },
                                {
                                    "label": "Workspace name",
                                    "value": "onna.canonical.content.resources.eslack.IESlack|workspace_name",
                                    "isSelected": True,
                                    "isHidden": True
                                }
                            ]
                        },
                        {
                            "label": "Workplace",
                            "children": [
                                {
                                    "label": "Workplace conversation ID",
                                    "value": "onna.canonical.content.resources.workplace.IWorkplace|thread_id",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Workplace conversation name",
                                    "value": "onna.canonical.content.resources.workplace.IWorkplace|thread_name",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Workplace conversation type",
                                    "value": "onna.canonical.content.resources.workplace.IWorkplace|thread_type",
                                    "isSelected": False,
                                    "isHidden": True
                                }
                            ]
                        },
                        {
                            "label": "XTag",
                            "children": [
                                {
                                    "label": "List of XTags",
                                    "value": "onna.canonical.behaviors.xtag.IXTag|tags",
                                    "isSelected": False,
                                    "isHidden": True
                                }
                            ]
                        },
                        {
                            "label": "Zendesk",
                            "children": [
                                {
                                    "label": "Group membership",
                                    "value": "onna.canonical.content.resources.zendesk.IZendesk|group",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Organization",
                                    "value": "onna.canonical.content.resources.zendesk.IZendesk|organization",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Tags",
                                    "value": "onna.canonical.content.resources.zendesk.IZendesk|tags",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Ticket ID",
                                    "value": "onna.canonical.content.resources.zendesk.IZendesk|thread_id",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Ticket name",
                                    "value": "onna.canonical.content.resources.zendesk.IZendesk|thread_name",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Ticket priority",
                                    "value": "onna.canonical.content.resources.zendesk.IZendesk|priority",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Ticket requester",
                                    "value": "onna.canonical.content.resources.zendesk.IZendesk|requester",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Ticket responsible",
                                    "value": "onna.canonical.content.resources.zendesk.IZendesk|assignee",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Ticket status",
                                    "value": "onna.canonical.content.resources.zendesk.IZendesk|status",
                                    "isSelected": False,
                                    "isHidden": True
                                },
                                {
                                    "label": "Ticket type",
                                    "value": "onna.canonical.content.resources.zendesk.IZendesk|thread_type",
                                    "isSelected": False,
                                    "isHidden": True
                                }
                            ]
                        }
                    ],
                    "use_original_filename": False,
                    "documentNumbering": {
                        "fieldName": {
                            "selected": False,
                            "viewValue": "ControlNumber",
                            "value": "ControlNumber"
                        },
                        "prefix": {
                            "selected": False,
                            "viewValue": "CN",
                            "value": "CN"
                        },
                        "startNumber": {
                            "selected": False,
                            "viewValue": "1",
                            "value": 1
                        },
                        "digits": {
                            "selected": False,
                            "viewValue": "8",
                            "value": 8
                        },
                        "groupIdentifierField": {
                            "selected": False,
                            "viewValue": "GroupId",
                            "value": "GroupID"
                        }
                    },
                    "volumeNumbering": {
                        "prefix": {
                            "selected": False,
                            "viewValue": "VOL",
                            "value": "VOL"
                        },
                        "startNumber": {
                            "selected": False,
                            "viewValue": "1",
                            "value": 1
                        },
                        "digits": {
                            "selected": False,
                            "viewValue": "3",
                            "value": 3
                        },
                        "maxSize": {
                            "selected": False,
                            "viewValue": "2000",
                            "value": 2000
                        }
                    },
                    "subdirectoryNumbering": {
                        "includeNatives": {
                            "selected": False,
                            "viewValue": "No",
                            "value": False
                        },
                        "exportTextSeparately": {
                            "selected": False,
                            "viewValue": "No",
                            "value": False
                        },
                        "textFileEncoding": {
                            "selected": False,
                            "viewValue": "UTF-8",
                            "value": "utf-8"
                        },
                        "nativeFolderName": {
                            "selected": False,
                            "viewValue": "NATIVE",
                            "value": "NATIVE"
                        },
                        "textFolderName": {
                            "selected": False,
                            "viewValue": "TEXT",
                            "value": "TEXT"
                        },
                        "startNumber": {
                            "selected": False,
                            "viewValue": "1",
                            "value": 1
                        },
                        "digits": {
                            "selected": False,
                            "viewValue": "3",
                            "value": 3
                        },
                        "maxFilesPerFolder": {
                            "selected": False,
                            "viewValue": "500",
                            "value": 500
                        }
                    },
                    "loadFileFormat": {
                        "format": {
                            "selected": False,
                            "viewValue": "csv",
                            "value": "csv"
                        },
                        "encoding": {
                            "selected": False,
                            "viewValue": "UTF-8",
                            "value": "utf-8"
                        },
                        "columnCharacter": {
                            "selected": False,
                            "viewValue": "&#44; (ASCII:44)",
                            "value": 44
                        },
                        "quoteCharacter": {
                            "selected": False,
                            "viewValue": "&#34; (ASCII:34)",
                            "value": 34
                        },
                        "newLineCharacter": {
                            "selected": False,
                            "viewValue": "&#10; (ASCII:10)",
                            "value": 10
                        },
                        "multivalueCharacter": {
                            "selected": False,
                            "viewValue": "&#59; (ASCII:59)",
                            "value": 59
                        },
                        "nestedCharacter": {
                            "selected": False,
                            "viewValue": "&#92; (ASCII:92)",
                            "value": 92
                        }
                    },
                    "scope_uuid": None,
                    "scope_query": {
                        "advanced": {
                            "and": [{
                                ">": [{
                                    "var": "date_modified"
                                }, f"{seven_days_ago}"]
                            }, {
                                "text_contains": [{
                                    "var": "path"
                                }, f"{path}"]
                            }, {
                                "text_contains": [{
                                    "var": "type_name"
                                }, "Resource"]
                            }]
                        }
                    },
                    "created_by": f"{username}",
                    "exportType": "advanced",
                    "name": f"{export_name}"
                }
            ],
            "@type": "Export"
        }
    payload = json.dumps(payload)
    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 201:
        jsonData = response.json()

# POST request to the @multiFileExport endpoint to run the export
        payload = {
            "title": f"{jsonData['@name']}",
            "resource_url": f"{jsonData['@id']}"
        }
        payload = json.dumps(payload)
        response = requests.request("POST", f"{base_url}/api/{container}/{account}/@multiFileExport",
                                    headers=headers, data=payload)
        if response.status_code == 200:
                print("Export created and now processing")
        else:
            print("Error found:")
            print(response.json())
    else:
        print("Error found:")
        print(response.json())
