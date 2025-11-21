CubeNet – Plan
==============

1. What CubeNet Is

CubeNet is a 3-dimensional neural reactor built around explosive signal propagation inside cubic neuron lattices. Instead of layers, it uses:

- Cubes (9×9×9 neuron grids) that ignite from a single injection point
- Front gates that shape the initial blast
- Back gates that judge the result and request refinements
- Retry loops where front & back gates slap signals back and forth until confident
- Chained cubes for multi-stage reasoning

CubeNet’s intelligence comes from geometry, chaos, boundary behavior, and feedback, not deep stacking.

2. Why It Exists

Because huge networks are boring and expensive, and ChaosNet proved that:

- dynamic systems
- death
- survival
- ticks
- chaotic mixing

…can do surprising work without massive parameter counts.

CubeNet is the next evolution: structured chaos with spatial meaning.

The cube shape gives:

- predictable wave propagation
- boundary behavior
- corner-edge-surface signatures
- spatial time encoding

This creates emergent intelligence even before training.

3. Core Components

3.1 Injector Neuron

- Takes the raw input.
- Does nothing fancy.
- Just sparks the reactor.

3.2 Front Gates (GateA, GateB)

- Sit right after the injector.
- Ignore the initial blast.
- Run small internal slaps (A↔B micro-updates).
- Refine the injection.
- Shape the input signal.
- Only release the packet into the cube when ready.
- React to back-gate feedback.

3.3 Cube (9×9×9 Reactor)

729 neurons arranged in 3D.

Each neuron connects to 26 neighbors (3D Moore adjacency): faces + edges + corners.

Effect:

- 1 neuron → 26 → 26² → full cube
- complete saturation in ~2 ticks

The cube creates a wavefront that hits edges and corners at different times. This timing becomes signal.

3.4 Back Gates (GateC, GateD)

- Read the compressed output of the cube.
- Compute confidence.
- Decide if the result is strong enough.
- If not, send feedback to front gates.
- Trigger “try again” cycles.
- Shape the cube’s compression before sending to next cube.

3.5 Retry Loop

If confidence < threshold:

- Back gates send a correction pulse.
- Front gates adjust their state.
- Front/back slap each other a few more rounds.
- Cube is reinjected with refined packet.
- Retries capped so system never spirals.

This is CubeNet’s “thinking” phase.

3.6 Cube2 and Beyond

Once Cube1 passes confidence:

- Packet flows through back gates.
- Into Cube2.
- Where the process repeats.
- Or the final readout happens.

Chained cubes amplify spatial intelligence.

4. How It Works (Signal Flow)

Step-by-step

1. Input → Injector Neuron: Raw signal becomes a scalar or tiny vector.
2. Front Gates Initialize: Front gates run a few A↔B slaps to form a starting state.
3. Front Gates Release Packet: Slapped signal is injected into center/front face of Cube1.
4. Cube1 Explodes: Signal fans out exponentially inside the 3D grid.
5. Cube1 Compresses: 729 → 2 (or 4) dimensional bottleneck.
6. Back Gates Read + Judge: Compute confidence via entropy/margin/SNR.
7. If confident → Move on: Packet proceeds to Cube2.
8. If not confident → Retry: Back gates send feedback to front gates. Front gates adjust and reinject. Process repeats up to max_retries.
9. Cube2 Explodes: Same process, but now with refined signal. (Optional more cubes.)
10. Final Readout: Output is fed to classification/regression head.

5. Why the Retry Mechanism Matters

Because cubes are chaotic. Raw explosions are messy. Sometimes the first blast is trash. Gates negotiate to find a better injection.

This creates:

- self-correction
- adaptive inference
- variable computation
- early/late exit
- confidence-aware reasoning

Like a mini prefrontal cortex in a box.

6. Training Strategy

6.1 What to Train

- Gate weights.
- Compressor/decompressor.
- Readout head.
- Optional cube mix weights.

Cubes themselves can remain mostly fixed reservoirs.

6.2 Loss

Task Loss + Retry Penalty + Gate Regularization.

6.3 Stabilization

- Tiny leak in gate states.
- Normalize bottleneck.
- Gradient clipping.
- Low learning rate on cube internals.

7. Why CubeNet Might Work

Because it mixes:

- structured chaos
- spatial wavefront dynamics
- boundary signatures
- compression bottlenecks
- dynamic retries

This is enough to produce:

- decision boundaries
- memory traces
- attractor states
- sensitivity to input deltas
- iterative refinement

It’s not a transformer or MLP. It’s a dynamical machine.

8. Risks / Challenges

- Too many retries = oscillation.
- Too few = underthinking.
- Unstable cube weights can blow up.
- Poor normalization kills training.
- Confidence metric is sensitive.

But nothing here is impossible. Just engineering.

9. Minimum Viable CubeNet (v1.0)

- 1 injector neuron.
- Front Gate A, Front Gate B.
- Cube1 (9×9×9).
- Back Gate C, Back Gate D.
- Retry loop.
- Cube2 (9×9×9).
- Readout head.

Start there. Add more cubes later.

10. Long-term Variants

- CubeNet-XL (multi-cube chain).
- CubeNet-Fission (extra chaotic rules).
- CubeNet-Delta (neurons die over time).
- CubeNet-Reflect (gates read cube surfaces).
- CubeNet-Temporal (cube ticks extended).

All fit the same base architecture.
