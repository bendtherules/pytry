from note_32 import note;
class notebook:
    def __init__(self):
        self.note_id=0;
        self.note_list=[];
        self.counter=0;
        self.return_list=[];
    def create_note(self,title,contents,tags=[]):
        self.note_id+=1;
        self.note_list.append(note(self.note_id,title,contents,tags));
    def search(self,term,where=None):
        self.return_list=[];#used for removing traces of previous search
        for self.counter in range(self.note_id):#range(x) means to 0 to x-1
            if self.note_list[self.counter].search(term):
                self.note_list[self.counter]._print_();#used for debugging
                self.return_list.append(self.counter+1);#return_list return a list of id's where search is successfull
        return self.return_list;
    def open_note(self,id,which="all"):
        self.note_list[id-1]._print_(which);

def main():
    pass

if __name__ == '__main__':
    main()
