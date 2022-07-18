CODE_EXAMPLES = {
    'python':'''import pandas as pd
 
COLUMN_NAMES = ['To','CC','BCC','Subject','Body']
 
def make_rows(  to:list = ['Any recipient email addresses'],
                cc:list = ['Any email addresses added by CC'],
                bcc:list = ['Any email addresses added by BCC'],
                subject:str = "Email's subject",
                body:str = "Email's body (HTML is supported)",
                **filters):
 
    """
    Make my rows!
 
    Each distro list should be delimited by ';' 
        EXAMPLE: garrett@uhaul.com; garrett2@uhaul.com
 
    Each required list arg must contain the same qty of variables
    """
 
    df = pd.dataframe(columns=COLUMN_NAMES) # this is my dataframe
 
    _filters = [ f'{key}={val}' for key,val in **filters.items() ]
    _filters = ';'.join( _filters )
 
    for i in to:''',
    'sql':'''select  'Any recipient email addresses' as [To], 
        'Any email addresses added by CC' as [CC], 
        'Any email addresses added by BCC' as [BCC], 
        "Email's subject" as [Subject], 
        "Email's body (HTML is supported)" as [Body]'''
}