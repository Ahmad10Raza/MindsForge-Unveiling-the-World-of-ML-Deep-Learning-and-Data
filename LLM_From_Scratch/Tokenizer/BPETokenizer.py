from collections import Counter

class BPETokenizer:
    def __init__(self, num_merges=50):
        self.num_merges = num_merges
        self.vocab = {}
        self.bpe_merges = []
        self.token2id = {}
        self.id2token = {}

    # Step 1: Build vocab from corpus
    def build_vocab(self, corpus):
        tokens = [list(word) + ["</w>"] for word in corpus]
        vocab = Counter([" ".join(token) for token in tokens])
        return vocab

    # Step 2: Count pair frequencies
    def get_stats(self, vocab):
        pairs = Counter()
        for word, freq in vocab.items():
            symbols = word.split()
            for i in range(len(symbols)-1):
                pairs[(symbols[i], symbols[i+1])] += freq
        return pairs

    # Step 3: Merge the most frequent pair
    def merge_vocab(self, pair, vocab):
        new_vocab = {}
        bigram = " ".join(pair)
        replacement = "".join(pair)
        for word in vocab:
            new_word = word.replace(bigram, replacement)
            new_vocab[new_word] = vocab[word]
        return new_vocab

    # Step 4: Train BPE
    def train(self, corpus):
        vocab = self.build_vocab(corpus)

        for i in range(self.num_merges):
            pairs = self.get_stats(vocab)
            if not pairs:
                break
            best = max(pairs, key=pairs.get)
            vocab = self.merge_vocab(best, vocab)
            self.bpe_merges.append(best)

        # Build final vocabulary
        tokens = set()
        for word in vocab:
            tokens.update(word.split())
        tokens = sorted(tokens)

        self.token2id = {tok: idx for idx, tok in enumerate(tokens)}
        self.id2token = {idx: tok for tok, idx in self.token2id.items()}

    # Step 5: Apply BPE to a single word
    def apply_bpe(self, word):
        symbols = list(word) + ["</w>"]
        for merge in self.bpe_merges:
            i = 0
            while i < len(symbols) - 1:
                if (symbols[i], symbols[i+1]) == merge:
                    symbols[i:i+2] = ["".join(merge)]
                else:
                    i += 1
        return symbols

    # Step 6: Encode text → tokens + IDs
    def encode(self, text):
        words = text.split()
        tokens = []
        ids = []
        for word in words:
            subwords = self.apply_bpe(word)
            tokens.extend(subwords)
            ids.extend([self.token2id[sub] for sub in subwords if sub in self.token2id])
        return tokens, ids

    # Step 7: Decode IDs → text
    def decode(self, ids):
        tokens = [self.id2token[i] for i in ids]
        text = "".join(tokens).replace("</w>", " ")
        return text.strip()

