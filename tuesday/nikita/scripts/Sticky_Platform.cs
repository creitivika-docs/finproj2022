using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Sticky_Platform : MonoBehaviour
{
    private void OnCollisionEnter2D(Collision2D collision)
    {
        if(collision.gameObject.name == "Player")
          {
            collision.gameObject.transform.SetParent(transform);
          }
    }
    private void OnCollisionExitr2D(Collision2D collision)
    {
        if(collision.gameObject.name == "Player")
          {
            collision.gameObject.transform.SetParent(null);
          }
    }
}
