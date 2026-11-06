import React from 'react';
import {Composition, AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig} from 'remotion';
const Hello: React.FC = () => {
  const f = useCurrentFrame(); const {fps} = useVideoConfig();
  const s = spring({frame: f, fps, config: {damping: 12}});
  const o = interpolate(f, [0, 10], [0, 1], {extrapolateRight: 'clamp'});
  return (<AbsoluteFill style={{background: '#0b0620', alignItems: 'center', justifyContent: 'center'}}>
    <div style={{color: '#fff', fontSize: 140, fontFamily: 'Arial', fontWeight: 800, opacity: o, transform: `scale(${0.6 + 0.4 * s})`}}>brand</div>
  </AbsoluteFill>);
};
export const Root: React.FC = () => <Composition id="Hello" component={Hello} durationInFrames={90} fps={60} width={1920} height={1080} />;
