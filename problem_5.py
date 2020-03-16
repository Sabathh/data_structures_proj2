import hashlib

from datetime import datetime, timezone

class Block:

  def __init__(self, data : str, previous_hash : str):
    self._timestamp = datetime.now(timezone.utc) # UTC is the same as GMT
    self._data = data # Implementation on accepts data as string
    self._previous_hash = previous_hash
    self._hash = self.calc_hash()

    self._next = None

  def calc_hash(self) -> str:
      """ Converts timestamp, data and previous_hash into a SHA256 hash.
          Hashing to sha256 has the complexity of O(n), since each character is visited once.
      
      Returns:
          string -- Hexadecimal SHA256 hash in string format
      """
      sha = hashlib.sha256()

      date_string = self.timestamp.strftime("%H:%M:%S %d/%m/%Y") # Convert date to string format
      
      hash_str = (date_string + " - "+ self.data  + " - " + self.previous_hash) # Assemble block info for hashing
      hash_str_utf8 = hash_str.encode('utf-8')
      
      sha.update(hash_str_utf8)

      return sha.hexdigest()

  @property
  def timestamp(self) -> datetime:
    return self._timestamp

  @property
  def data(self) -> str:
    return self._data

  @property
  def next(self) -> 'Block':
    return self._next
  
  @next.setter
  def next(self, next_block : 'Block'):
    self._next = next_block

  @property
  def hash(self) -> str:
    return self._hash

  @property
  def previous_hash(self) -> str:
    return self._previous_hash

class Blockchain:

  def __init__(self):
    self.head = None

  def append(self, data : str):
    """ Crates block containing the specified data and appends it to the end of the blockchain
        Requires traversing the list. O(n)
    
    Arguments:
        data {str} -- Data to be stored in the blockchain
    
    Raises:
        ValueError: Error raised in an invalid block is found in the blockchain
    """
    # Creates a head if there is none
    if self.head is None:
        self.head = Block(data, "0")
        return

    block = self.head
    
    # Finds the last block in the chain
    while block.next is not None:
      previous_hash = block.hash # Stores block's hash before retrieving new block
      block = block.next

      # Validates current block
      if not self.validate_block(block, previous_hash):
        raise ValueError('Found invalid block"') # Not sure which error is more appropriate
      
    # Adds new block to the end of the chain  
    block.next = Block(data, block.hash)

  def validate_block(self, block : Block, hash : str) -> bool:
    """ Returns whether provided block has the correct hash of the previous block
        Simply compares the values. Complexity of O(1)
    Arguments:
        block {Block} -- Block to be validated
        prevoius_hash {str} -- Hash of the previous block
    
    Returns:
        bool -- True if block is valid. Otherwise, false.
    """
    return block.previous_hash == hash


def test_block():
  # Test first block
  block1 = Block("data1", "0")
  assert(block1.data == "data1")
  assert(type(block1.timestamp) == datetime)
  assert(block1.previous_hash == "0")

  # Test next block in chain
  block2 = Block("data2", block1.hash)
  assert(block2.data == "data2")
  assert(type(block2.timestamp) == datetime)
  assert(block2.previous_hash == block1.hash)

  print("Blocks are fine!")

def test_blockchain(data_list : list):
  # Create entire blockchain and checks if all values in data_list were included as blocks
  blockchain = Blockchain()

  for data in data_list:
    blockchain.append(data)

  block = blockchain.head
  index = 0
  while block is not None:
    assert(block.data == data_list[index])
    block = block.next
    index += 1
  

if __name__ == "__main__":
  test_block()
  print("Testing single block in chain")
  test_blockchain(["data"])
  print("Testing big block in chain")
  test_blockchain(["biglargehugeamountofdatainasingleblock123456789qwertyuiopasdfghjklzxcvbnm"])
  print("Testing 3 blocks in chain")
  test_blockchain(["data1", "data2", "data3"])
  print("Testing 10 blocks in chain")
  test_blockchain(["data1", "data2", "data3", "data4", "data5", "data6", "data7", "data8", "data9", "data10"])
  print("Blockchain is fine")

