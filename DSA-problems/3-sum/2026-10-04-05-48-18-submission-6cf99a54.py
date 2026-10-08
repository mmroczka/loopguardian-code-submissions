# Managed by BeyondCTCI one-way sync (force-pushed). Manual edits are not reconciled and may be overwritten by future syncs.
def three_sum(arr, w):
  arr = sorted(arr)
  n = len(arr)
  for i in range(n - 2):
    lo, hi = i + 1, n - 1
    while lo < hi:
      s = arr[i] + arr[lo] + arr[hi]
      if s == w:
        return True
      if s < w:
        lo += 1
      else:
        hi -= 1
  return False
