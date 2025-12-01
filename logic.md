## Step 1 - Image
Take the image and convert it into a 2d array of RGB values.

## Step 2 - Scaling
### 3x3 -> 1 case
| a | b | c |
|---|---|---|
| d | e | f | 
| g | h | i |

| abcdefghi |
|-----------|
### 3x3-> 2x2
| a | b | c |
|---|---|---|
| d | e | f | 
| g | h | i |

| abde | bcef |
|------|------|
| degh | ehfi |


### 4x4 -> 2x2
| a | b | c | d |
|---|---|---|---|
| e | f | g | h |
| i | j | k | l |
| m | n | o | p |

| abef | cdgh |
|------|------|
| ijmn | klop |

### 4x4 -> 3x3
| a | b | c | d |
|---|---|---|---|
| e | f | g | h |
| i | j | k | l |
| m | n | o | p |

| abef | bcfg | cdgh |
|------|------|------|
| efij | fgjk | ghkl | 
| ijmn | jkno | klop |

Every time, consistent number of pixels being averaged

Subspace size is ceiling (Og / New)  
Traversal length is subspace length if no ceiling needed, but subspace length -1 if division was not 

## Non-Square
### 7x2 -> 3x1
| a | b | c | d | e | f | g |
|---|---|---|---|---|---|---|
| h | i | j | k | l | m | n |

| abchij | cdejkl | efglmn |
|--------|--------|--------|