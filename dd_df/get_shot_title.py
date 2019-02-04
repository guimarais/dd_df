import dd

def get_shot_title(shotnr, with_shotnr=True):
    """Returns the shot title as it is stored in the JOU diagnostic"""
    jou = dd.shotfile('JOU', shotnr)
    umb = jou.getParameter('REMARKS', 'REMARKS')
    jou.close()
    ##Remove first characters
    umb2 = umb.data[4:]
    umb3 = umb2.tostring()
    if with_shotnr:
        title = '\#' + str(shotnr) + ' ' + umb3.splitlines()[0]
    else:
        title = umb3.splitlines()[0]
    return str(title)
