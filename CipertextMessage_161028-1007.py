class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        '''
        Message.__init__(self, text)

    def decrypt_message(self):
        '''        
        '''
        dict0 = {}
        best0 = 0
        list1 = load_words('words.txt')

        for shift0 in range(26):
            # APPLY SHIFT (0-26) to MSG IN INPUT  
            str0 = self.apply_shift(shift0)
            
            # COUNT NBR REAL WORD IN CYPHERED TXT
            list0 = str0.split(' ')
            count0 = 0
            for i0 in list0:
                if is_word(list1, i0):
                    count0 += 1
            list0 = []
            
            # STORE SHIFT, NBR REAL WORD, DECRYPTED TXT
            dict0[shift0]= (count0, str0)

            # STORE BIGGER COUNT NBR WITH RELATED SHIFT
            if best0 < count0:
                best0 = count0
                best1 = shift0
            
        return dict0[best1][:]
        
        
        
