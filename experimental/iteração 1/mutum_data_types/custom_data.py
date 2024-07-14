from typing import List, Dict, Optional

class Custom_data:# For a single static formatted data used in documents, prints and simple usage
    def __init__(self, name: str, format_counter: List[Dict[str, int]], size_wo_dividers: int, format_divider: Optional[List[Dict[str, str]]] = None) -> None:
        """
        Initializes the Custom_data object.

        :param name: Identification of the data
        :param format_counter: List of dictionaries representing segment lengths.
                               Each dictionary should have a 'name' key (optional) and a 'length' key.
                               Example: [{'name': 'country_code', 'length': 2}, {'length': 2}, {'length': 1}, {'length': 4}, {'length': 4}]
                               If 'name' is not provided, 'segment' is used as the default name.
        :param format_divider: List of dictionaries representing dividers.
                               Each dictionary should have a 'name' key (optional) and a 'divider' key.
                               Example: [{'divider': '+'}, {'divider': ' '}, {'divider': ' '}, {'divider': ' '}, {'divider': '-'}]
                               If 'name' is not provided, 'divider' is used as the default name.
        :param size_wo_dividers: Expected size for the data without dividers
        """
        if format_divider is None:
            format_divider = []
        
        if len(format_counter) not in {len(format_divider), len(format_divider) + 1}:
            raise ValueError("Length of format_counter must be equal to or one more than the length of format_divider")
        
        if sum(segment.get('length', 0) for segment in format_counter) != size_wo_dividers:
            raise ValueError("Sum of format_counter lengths must equal size_wo_dividers")

        self.__name = name  # Identification of the data
        self.__format_counter = [{'name': segment.get('name', 'segment'), 'length': segment['length']} for segment in format_counter]  # List of dictionaries with segment names and lengths
        self.__format_divider = [{'name': divider.get('name', 'divider'), 'divider': divider['divider']} for divider in format_divider]  # List of dictionaries with divider names and dividers
        self.__size_wo_dividers = size_wo_dividers  # Expected size for the data without dividers
        self.__value = None  # Data storage

    # Accessor methods (getters)
    def get_name(self) -> str:
        return self.__name

    def get_format_counter(self) -> List[Dict[str, int]]:
        return self.__format_counter

    def get_format_divider(self) -> List[Dict[str, str]]:
        return self.__format_divider

    def get_size_wo_dividers(self) -> int:
        return self.__size_wo_dividers

    def get_value(self) -> str:
        return self.__value

    # Mutator methods (setters)
    def set_name(self, name: str) -> None:
        self.__name = name

    def set_format_counter(self, format_counter: List[Dict[str, int]]) -> None:
        self.__format_counter = [{'name': segment.get('name', 'segment'), 'length': segment['length']} for segment in format_counter]

    def set_format_divider(self, format_divider: List[Dict[str, str]]) -> None:
        self.__format_divider = [{'name': divider.get('name', 'divider'), 'divider': divider['divider']} for divider in format_divider]

    def set_size(self, size: int) -> None:
        self.__size_wo_dividers = size

    def set_value(self, value: str) -> None:
        if len(value) != self.__size_wo_dividers:
            raise ValueError("Value length does not match the expected size")
        self.__value = value

    # Method to format the stored data based on the provided format_counter and format_divider
    def format_data(self) -> str:
        if self.__value is None:
            raise ValueError("No value set for formatting")
        
        if len(self.__value) != self.__size_wo_dividers:
            raise ValueError("Stored data length does not match the expected size")

        formatted_data = ""
        data_index = 0
        for i, segment in enumerate(self.__format_counter):
            length = segment['length']
            if length > 0:
                formatted_data += self.__value[data_index:data_index + length]
                data_index += length
            if i < len(self.__format_divider):
                formatted_data += self.__format_divider[i]['divider']
        return formatted_data