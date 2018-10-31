class CommonFunctions:

    def delete_null_dict_items(input_dict):
        cleaned_dict = dict()
        for now in input_dict:
            if input_dict[now] != None:
                cleaned_dict.update({now: input_dict[now]})

        return cleaned_dict