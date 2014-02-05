import time;
class note:
    def __init__(self,note_id,title,contents,tags=[]):
        self.id=note_id;
        self.title=title;
        self.contents=contents;
        self.tags=tags;
        self.creationtime=time.localtime();
        #tm_year,tm_mon,tm_mday,tm_hour,tm_min,tm_sec supported
    def search(self,term,where=None):
        ''' "term" is the search term.
             "where" is supported to search for only in title or contents or
             tags -currently unused.
             Currently searches for a whole word-better than searching
             for letters'''
        #ToDo1 search for the whole string and perfect match .. actually use
        #option for partial and whole check
        #ToDO2 make sure all checkings are string type or atleast permissible after notebook class
        #ToDo3 implement "where" in this function
        return bool(self.title.split(" ").count(term)) or bool(self.contents.split(" ").count(term)) or bool(self.tags.count(term)) ;
    def  edit(self,title="",contents="",tags=[],choice=1):

        '''Only mention required parameters.Choice must be given. Choice: 1 for replace, 2 for append.
           Call example:edit(title="untitled",choice=1) will make the title "untitled". Rest unaffected'''
        if title!="":
            if choice==1:
                self.title=title;
            elif choice==2:
                self.title+=title;
        if contents!="":
            if choice==1:
                self.contents=contents;
            elif choice==2:
                self.contents+=contents;
        if tags!=[]:
            if choice==1:
                self.tags=tags;
            elif choice==2:
                self.tags+=tags;
        self.creationtime=time.localtime();

    def _print_(self,which="all"):
        #To print the details for debugging purpose..working
        if which=="all":
            print ("Id="+str(self.id)+"\nTitle="+self.title+"\ncontents="+self.contents+"\ntags="+str(self.tags)+"\ncreationtime="+str(self.creationtime));
        else:
            print (which+"=",end='');# end='' is used to print without newline
            exec("print(str(self."+which+"))");

def main():
    pass

if __name__ == '__main__':
    main()
