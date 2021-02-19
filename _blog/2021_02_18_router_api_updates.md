---
title: 'Minor Router API updates'
date: 2021-02-18
permalink: /blog/2020/02/minor-router-api-updates/
tags:
  - minor update
  - development
  - api update

---

We have updated the Router API to make it cleaner. This applies to Raphtory (? How do we refer to this without version numbers) onwards. Previously the coder needed to say SendUpdate and wrap this around the type of update that was being performed. The API now simply allows the user to directly make the update.

The new API looks like this.
To add a vertex or edge (where "Vertex/Edge Type/Property" etc can be any string)

```
VertexAdd(timeStamp,srcID,Type("Vertex Type"))
VertexAddWithProperties(timeStamp, srcID, Properties(ImmutableProperty("Vertex Property",sourceNode)),Type("Vertex Type")))
EdgeAdd(timeStamp,srcID,tarID,Type("Some Edge Type"))
EdgeAddWithProperties(timeStamp,srcID,tarID,Properties(ImmutableProperty("Edge Property",sourceNode)),Type("Edge Type")))
```

To remove a vertex or edge:

```
deleteVertex(msgTime, srcId)
EdgeDelete(msgTime, srcId, dstId)
```

So previously your code might look like this:
```
sendUpdate(VertexAddWithProperties(timeStamp, srcID, Properties(ImmutableProperty("name",sourceNode)),Type("Character")))
sendUpdate(VertexAddWithProperties(timeStamp, tarID, Properties(ImmutableProperty("name",targetNode)),Type("Character")))
sendUpdate(EdgeAdd(timeStamp,srcID,tarID, Type("Character Co-occurence")))
```

Your updated code should look like this:
```
VertexAddWithProperties(timeStamp, srcID, Properties(ImmutableProperty("name",sourceNode)),Type("Character"))
VertexAddWithProperties(timeStamp, tarID, Properties(ImmutableProperty("name",targetNode)),Type("Character"))
EdgeAdd(timeStamp,srcID,tarID, Type("Character Co-occurence"))
```

Hopefully code updates should be extremely simple. 
