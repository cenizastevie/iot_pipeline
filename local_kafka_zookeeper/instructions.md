Sometimes we receive errors like:

```
org.apache.zookeeper.KeeperException$NodeExistsException: KeeperErrorCode = NodeExists
```

To resolve this, run the following command:

```bash
docker compose down --volumes
```