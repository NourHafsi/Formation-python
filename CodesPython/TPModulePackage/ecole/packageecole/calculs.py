def moyenne(note):
    M= sum(note)/len(note)
    return M
def Validation(moyenne):
    if moyenne >= 10:
        print("admis")
    else:
        print("redoublant")



    