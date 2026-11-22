import argparse, json
import numpy as np

def triangulate(rays):
    '''Each row is [origin XYZ, direction XYZ] in a shared right-handed frame.'''
    rows=np.asarray(rays,dtype=float)
    if rows.ndim!=2 or rows.shape[0]<2 or rows.shape[1]!=6 or not np.isfinite(rows).all():
        raise ValueError('Supply two or more finite [x,y,z,dx,dy,dz] rows')
    origins=rows[:,:3]; directions=rows[:,3:]
    norms=np.linalg.norm(directions,axis=1)
    if (norms<1e-12).any(): raise ValueError('Zero direction')
    directions=directions/norms[:,None]
    projectors=np.eye(3)-directions[:,:,None]*directions[:,None,:]
    a=projectors.sum(axis=0)
    if np.linalg.cond(a)>1e8: raise ValueError('Rays too close to parallel')
    b=np.einsum('nij,nj->i',projectors,origins)
    point=np.linalg.solve(a,b)
    if (((point-origins)*directions).sum(axis=1)<0).any():
        raise ValueError('Intersection lies behind an observer')
    errors=np.linalg.norm(np.cross(point-origins,directions),axis=1)
    return {'xyz':point.tolist(),'rms':float(np.sqrt(np.mean(errors**2)))}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('rays',type=argparse.FileType('r'));args=p.parse_args()
    print(json.dumps(triangulate(json.load(args.rays)),indent=2))
