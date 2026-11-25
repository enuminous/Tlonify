-- Proposed formal sketch; compilation not verified.
namespace Tlonification
def backlog (q g v : Nat) : Nat := q + g - v
theorem zero_backlog (q g v : Nat) (h : q + g ≤ v) :
    backlog q g v = 0 := by
  exact Nat.sub_eq_zero_of_le h
end Tlonification
