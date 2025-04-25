def decode_message(encoded_message):
    def decode_helper(s, index, current_decoding, all_decodings):
        if index == len(s):
            all_decodings.append(current_decoding)
            return
        
        if s[index] != '0':
            decode_helper(s, index + 1, current_decoding + chr(int(s[index]) + 64), all_decodings)
        
        if index + 1 < len(s) and s[index] != '0' and int(s[index:index + 2]) <= 26:
            decode_helper(s, index + 2, current_decoding + chr(int(s[index:index + 2]) + 64), all_decodings)
    
    all_decodings = []
    decode_helper(encoded_message, 0, "", all_decodings)
    return all_decodings

encoded_message = "11106"
decoded_messages = decode_message(encoded_message)
for message in decoded_messages:
    print(message)