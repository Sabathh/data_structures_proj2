import hashlib

import datetime

class Block:

    def __init__(self, data, previous_hash):
      self.timestamp = datetime.datetime.now() # /TODO: Make timestamp only use GMT time 
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
  
    def calc_hash(self):
        """ Converts timestamp, data and previous_hash into a SHA256 hash
        
        Returns:
            string -- Hexadecimal SHA256 hash in string format
        """
        sha = hashlib.sha256()

        date_string = self.timestamp.strftime("%H:%M:%S %d/%m/%Y") # Convert date to string format
        
        hash_str = (date_string + " - "+ self.data  + " - " + self.previous_hash) # Assemble block info for hashing
        hash_str_utf8 = hash_str.encode('utf-8')
        
        sha.update(hash_str_utf8)

        return sha.hexdigest()

def test_block():
  # Test first block
  block1 = Block("data1", "0")

  assert(block1.data == "data1")
  assert(type(block1.timestamp) == datetime.datetime)
  assert(block1.previous_hash == "0")

  # Test next block in chain
  block2 = Block("data2", block1.hash)
  assert(block2.data == "data2")
  assert(type(block2.timestamp) == datetime.datetime)
  assert(block2.previous_hash == block1.hash)

  print("Blocks are fine!")


def main():
  test_block()

if __name__ == "__main__":
  main()
