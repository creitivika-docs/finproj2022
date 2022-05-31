using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Finish : MonoBehaviour
{
    private AudioSource FinishSound;

    private bool LevelCompleted = false;

    public ParticleSystem Confetti;

    public Animator Transition;

    private void Start()
    {
        FinishSound = GetComponent<AudioSource>();
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if(collision.gameObject.name == "Player" && !LevelCompleted)
          {
            FinishSound.Play();
            LevelCompleted = true;
            Invoke("CompleteLevel", 2f);
            Transition.SetTrigger("Start");
            Confetti.Play();
          }
    }

    private void CompleteLevel()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 1);
    }
}
