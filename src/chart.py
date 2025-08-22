
VALID_NUMS  = [1,2,3,4,5,6,7,8,9]
MASTER_NUMS = [11,22]
KARMIC_NUMS = [13,14,16,19]

# Numerology Chart class containing the general template for creating, modifying, printing, and saving a numerological chart

class NumerologyChart():
    def __init__(self, date, name):
        self.date = date
        self.name = name

        # Date derived numbers
        self.life_path_num  = None
        self.birthday_num   = None
        self.challenge_num  = None

        # Name derived numbers
        self.expression_num     = None
        self.hearts_desire_num  = None
        self.personality_num    = None

        # Generate chart numbers
        self._generate_life_path()


    # Generate and store the lifepath number for self based on self.date
    def _generate_life_path(self) -> None:
        self.life_path_num = self.generate_life_path(self.date)

    # Takes date string in the form of "MMDDYYYY", ex: "03191995"
    # Returns life path number by adding the digits of each and reducing
    @staticmethod
    def generate_life_path(date: str) -> list[str]:
        # Divide up the date string into its subcomponents Month, Day, Year
        # in list format ["MM","DD","YYYY"]
        print(date)
        date_list = []
        date_list.append(date[0:2])
        date_list.append(date[2:4])
        date_list.append(date[4:8])
        print(date_list)

        return NumerologyChart.reduce_number(date_list)
    
        
    # Takes a list of string numbers and reduces them by adding their component integers
    # together until a number from 1-9, 11/22, or a karmic number (if selected) is reached. 
    # Ex. 39 -> 3+9 -> 12 -> 1+2 -> 3
    # Performs reduction on list items and then performs the same operation to combine all list
    # items to get one resulting string list. 
    # If normal number just one item will be returned (ex. ["8"]). If master or karmic number, 
    # two numbers will be returned (ex. ["22","4"])
    @staticmethod
    def reduce_number(
            num_list: list[str], 
            calculate_karmic_num: bool = False
        ) -> list[str]:
    
        # Inner recursive function that combines the integer values
        def reduce(
                num: str, 
                calc_karmic: bool= False
            ) -> list[int]:

            # Check number before reduction
            reduced = 0
            for n in str(num):
                reduced += int(n)
            
            # Return Master number (return master num and reduction)
            if int(num) in MASTER_NUMS:
                return [int(num),reduced]
            # Return Karmic number if calc_karmic True (return karmic num and reduction)
            elif int(num) in KARMIC_NUMS and calc_karmic:
                return [int(num),reduced]
            # If base num (1-9) return
            elif reduced in VALID_NUMS:
                return [reduced]            
            # Otherwise reduce further
            else:
                return reduce(reduced)

        

        # Reduce each number in num list, add their results and reduce again
        sum = 0
        for num in num_list:
            res = reduce(num)
            sum += res[0]

        final_reduction = reduce(sum)
        print(final_reduction)

        return final_reduction 


if __name__ == "__main__":
    #date = "04071996"    #Cass - 9
    #date = "03191995"    #David - 1
    #date = "05291948"    #Test - 11/2
    #date = "10221985"    #Ja - 1
    #date = "12121994"    #Jerrad - 11/2
    date = "04021996"    #Michelle - 4 

    ex_chart = NumerologyChart(date,None)