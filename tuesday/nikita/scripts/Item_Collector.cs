using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class Item_Collector : MonoBehaviour
{
    public int coins = 0;

    [SerializeField] private Text coinsText;
    [SerializeField] private AudioSource Collect;

    private void OnTriggerEnter2D(Collider2D collision)
    {
      if (collision.gameObject.CompareTag("Coin"))
        {
          Destroy(collision.gameObject);
          coins++;
          coinsText.text = "" + coins;
          Collect.Play();
        }
    }
}
