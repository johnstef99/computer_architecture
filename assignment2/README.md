# Assignment 2

## Βήμα 1

### Ερώτημα 1

Τρέχοντας τα benchmark με τα default options, με την χρήση του [script](./gem5_outputs/get_data.sh) παίρνουμε τα εξής δεδομένα:
| **Key** | **Value** |
| :-------------------------- | :-------: |
| **L1 icache size** | 32kB |
| **L1 icache associativity** | 2 |
| **L1 dcache size** | 64kB |
| **L1 dcache associativity** | 2 |
| **L2 cache size** | 2MB |
| **L2 cache associativity** | 8 |
| **Cache Line size** | 64 |

Γενικά τα δεδομένα που κάνει output το [script](./gem5_outputs/get_data.sh) είναι στην μορφή
`benchmark_clockSpeed_CacheLineSize_icacheSize_icacheAssoc_dcacheSize_dcacheAssoc_l2CacheSize_lwCacheAssoc`
Άρα τα default options είναι `2GHz_64_32kB_2_64kB_2_2MB_8`

### Ερώτημα 2

Με την χρήση αυτού του [script](./gem5_outputs/step1_q2.py) παίρνουμε τα εξής σχεδιαγράμματα:
![](./graphs/step1/sim_sec_2GHz_64_32kB_2_64kB_2_2MB_8.png)
![](./graphs/step1/cpi_2GHz_64_32kB_2_64kB_2_2MB_8.png)
![](./graphs/step1/icache_miss_rate_2GHz_64_32kB_2_64kB_2_2MB_8.png)
![](./graphs/step1/dcache_miss_rate_2GHz_64_32kB_2_64kB_2_2MB_8.png)
![](./graphs/step1/l2_cache_miss_rate_2GHz_64_32kB_2_64kB_2_2MB_8.png)

##### Παρατηρήσεις

- Τα benchmark με τα μεγαλύτερα cpi έχουν και μεγαλύτερο χρόνο εκτέλεσης καθώς και πολλά misses στην L1 dcache και L2 cache
- Το speclbm και specsjeng έχουν σχεδόν πάντα miss στην L2 cache

### Ερώτημα 3

Τρέχοντας ένα benchmark με default options βλέπουμε το `system.clk_domain.clock = 1000` δηλαδή το ρολόι χρονισμού του host
system είναι 1GHz και το `system.cpu_clk_domain = 500` δηλαδή το ρολόι χρονισμού του simulated cpu είναι 2GHz.
Τρέχοντας ξανά το benchmark με `--cpu-clock=1GHz` βλέπουμε το `system.clk_domain.clock = 1000` δηλαδή ίδιο με πριν
και το `system.cpu_clk_domain = 1000` δηλαδή το ρολόι χρονισμού του simulated cpu έγινε 1GHz.

Βλέποντας τα διαγράμματα για options `1GHz_64_32kB_2_64kB_2_2MB_8`:
![](./graphs/step1/sim_sec_1GHz_64_32kB_2_64kB_2_2MB_8.png)
![](./graphs/step1/cpi_1GHz_64_32kB_2_64kB_2_2MB_8.png)
![](./graphs/step1/icache_miss_rate_1GHz_64_32kB_2_64kB_2_2MB_8.png)
![](./graphs/step1/dcache_miss_rate_1GHz_64_32kB_2_64kB_2_2MB_8.png)
![](./graphs/step1/l2_cache_miss_rate_1GHz_64_32kB_2_64kB_2_2MB_8.png)
Παρατηρούμε ότι υπάρχει τέλειο scaling αφού μειώνοντας το clock στο μισό τα benchmarks χρειάστηκαν στον διπλάσιο χρόνο.
Εκτός απο τα speclbm και specsjeng που λόγω των πολλών miss στην L2 cache υπάρχει καθυστέρηση ανεξάρτητη του clock.

# Βήμα 2

Από το 1ο βήμα της εργασίας σχετικά με τα CPI, L1 data και instruction miss rates, L2 miss rates και simulated
seconds προέκυψαν ορισμένα γραφήματα.
Με τη βοήθειά τους, μπορούμε να προχωρήσουμε σε συγκεκριμένες αλλαγές των χαρακτηριστικών της για την
βελτιστοποίηση του CPI. Για παράδειγμα, το specbzip έχει υψηλά L1 data miss rates και L2 cache miss rates.
Επομένως, για τη μείωση του CPI, θα πρέπει να αλλάξουμε τo μέγεθος και associativity της L1 data cache για
την πρώτη περίπτωση, και τo μέγεθος και associativity της L2 για τη δεύτερη. Με την ίδια λογική συνεχίζει
και η ακόλουθη ανάλυση :

## Ανάλυση

### Specbzip

Απαιτείται κυρίως αλλαγή της L1 data cache και L2 cache.

Από το αρχείο με τα L1 data miss rate, για την L1 data cache προτείνονται οι βελτιώσεις:

- Αύξηση του μεγέθους(από τα 64kB σε 128kB)
- Αύξηση του associativity (από 2 σε 8)
- Αύξηση του μεγέθους της cache line (από 64 σε 128)

Από το αρχείο σχετικά με το L2 miss rate, για την L2 cache προτείνονται οι βελτιώσεις:

- Αύξηση του assocciativity (ουσιαστικά σταθεροποίηση στο default option 8 αν όχι ακόμη μεγαλύτερο που γενικά αντενδείκνυται -βλ. βήμα 3ο-)
- Αύξηση του μεγέθους cache line (από 64Β σε 128Β)

![](./graphs/step2/specbzip/cpi_specbzip.png)
[Περισσότερα διαγράμματα](./graphs/step2/specbzip/)

### Specmcf

Απαιτείται κυρίως αλλαγή της L1 instruction cache.

Από το αρχείο με τα L1 instruction miss rate, για την L1 instruction cache προτείνονται οι βελτιώσεις:

- Αύξηση του μεγέθους (από 32kB σε 128kB)
- Αύξηση του assocciativity (από 2 σε 8)

![](./graphs/step2/specmcf/cpi_specmcf.png)
[Περισσότερα διαγράμματα](./graphs/step2/specmcf/)

### Spechmmer

Απαιτείται κυρίως αλλαγή της L1 instruction cache (παρότι είναι από τα προγράμματα που εκτελέστηκαν
αποτελεσματικότερα για τα default χαρακτηριστικά cpu από τον gem5 δίνοντας το μικρότερο CPI μεταξύ των benchmarks).

Από το αρχείο με τα L1 instruction miss rate, για την L1 instruction cache προτείνονται οι βελτιώσεις:

- Αύξηση του μεγέθους (από 32kB σε 128kB)
- Αύξηση του associativity (από 2 σε 8)

![](./graphs/step2/spechmmer/cpi_spechmmer.png)
[Περισσότερα διαγράμματα](./graphs/step2/spechmmer/)

### Specsjeng

Απαιτείται κυρίως αλλαγή της L1 data cache και της L2 cache.

Από το αρχείο με τα L1 data cache miss rate, για τις caches προτείνεται:
specsjeng
- Αύξηση του μεγέθους cache line (από 64Β σε 128B)

Από το αρχείο με τα L2 cache miss rate, η αύξηση του μεγέθους και του associativity
έχει αμελητέα διαφορά στο L2 miss rate και γι' αυτό οι προτεινόμενες αλλαγές για το
συγκεκριμένο benchmark περιορίζονται στην παραπάνω αλλαγή του μεγέθους της cache line.

![](./graphs/step2/specsjeng/cpi_specsjeng.png)
[Περισσότερα διαγράμματα](./graphs/step2/specsjeng/)

### Speclbm

Απαιτείται κυρίως αλλαγή της L1 data cache και της L2 cache.

Από το αρχείο με τα L1 data cache miss rate, για τις caches προτείνεται:

- Αύξηση του μεγέθους της cache line (από 64B σε 128Β)

Παρόμοια με το αρχείο των L2 cache miss rates για το specjeng, έτσι και για το αρχείο των L2 cache
miss rates για το speclibm φαίνeται οτι με αύξηση του μεγέθους της L2 cache ή του associativity
υπάρχει αμελητέα βελτίωση του L2 miss rate. Για λόγο αυτό, οι προτάσεις βελτίωσης περιορίζονται και
για αυτό το benchmark στην παραπάνω αλλαγή της αύξησης του μεγέθους της cache line.

![](./graphs/step2/speclbm/cpi_speclbm.png)
[Περισσότερα διαγράμματα](./graphs/step2/speclbm/)

## Παρατηρήσεις:

1. Στις περιπτώσεις benchmarks που μειονεκτήματα είναι τα μεγάλα miss rates σε L1 (data ή και instruction) και L2 cache φαίνεται οτι η αύξηση των αντίστοιχων μεγεθών cache και του associativity αίρει αυτά τα μειονεκτήματα και, κατα συνέπεια, οδηγεί σε καλύτερο CPI. Τέτοια benchmarks είναι τα specbzip και specmcf.
2. Ωστόσο, υπάρχουν και benchmarks που δεν υπάγονται στην παραπάνω κατηγορία, αφού σε αυτά, η αύξηση του μεγέθους των caches δε φαίνεται να οδηγεί σε μείωση του CPI. Τα specjeng και speclibm αποτελούν χαρακτηριστικά παραδείγματα. Κοινό χαρακτηριστικό και των δύο είναι η άκαμπτη αντίδραση των L2 miss rates στην αύξηση του μεγέθους και του associativity της L2. Σε αυτά, μόνο η αύξηση του μεγέθους της cache line φαίνεται να οδηγεί στο βέλτιστο CPI.
3. Συνοψίζοντας, από την ανάλυση του CPI του προσωμοιούμενου επεξεργαστή για τις διάφορες παραμέτρους του, προκύπτει οτι η βελτιστοποίησή του για το εκάστοτε benchmark περιστρέφεται γύρω από τον άξονα της αύξησης των μεγεθών και του associativity των caches. Η αύξηση του μεγέθους της cache lines συντελεί στον ίδιο σκοπό.
