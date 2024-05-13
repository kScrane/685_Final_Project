ReadVUA.python : returns file "counts_of_metaphors" with literal vs metaphorical counts
    - simplified_data(dataset_name, modified_dataset)
    - remove_columns(dataset_name, modified_dataset)
    - count_metaphor_occurances(modified_dataset_name, counts_of_metaphors, record_count)

Merriam-Web_API.py <API Key> : takes tsv list of words to query MW for, writes files to JSON_obj_MW
    - parse_json_obj()
    - combine_json_obj(input_file, list_of_words, key)
    - get_literal_sentence(word, key)
    - get_words(input_file, min, max)

GetBasicSentences.py: Looks through MW results for sentences, store results in VUA20-BasicSentences
    - getAllBasicSentences(): loops through all JSON obj files + records sentences
    - getBasicSentences(json_sentences, data_file_name)

FormatBasicSentences.py:
    - formatSentences(input, output): saves metaphor bool, sentence, w_index in standard tsv
    - formatBasicSentences(): calls formatSentences on file
