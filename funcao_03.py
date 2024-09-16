import hashlib
import time

def findNonce(dataToHash, bitsToBeZero):
    nonce = 0
    start_time = time.time()
    
    while True:
        nonce_bytes = nonce.to_bytes(4, 'big')
        input_bytes = nonce_bytes + dataToHash
        hash_result = hashlib.sha256(input_bytes).digest()
        zero_bits = countLeadingZeroBits(hash_result)
        
        if zero_bits >= bitsToBeZero:
            end_time = time.time()
            elapsed_time = end_time - start_time
            return nonce, elapsed_time
        
        nonce += 1

def countLeadingZeroBits(byte_data):
    count = 0
    for byte in byte_data:
        if byte == 0:
            count += 8
        else:
            mask = 0x80
            while mask & byte == 0:
                count += 1
                mask >>= 1
            break
    return count